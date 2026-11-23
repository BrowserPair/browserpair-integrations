#!/usr/bin/env python3
"""Check BrowserPair's public integration packages without network access."""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN_URL = "https://chatgpt.com/plugins/plugin_asdk_app_6ac5859a310c8191b959b4cfd69b2668"
REGISTRY_URL = "https://github.com/mcp/com.browserpair/browserpair"
MCP_URLS = {"https://mcp.browserpair.com", "https://mcp.browserpair.com/mcp"}
errors = []


def check(ok, message):
    if not ok:
        errors.append(message)


def get_json(path):
    try:
        return json.loads((ROOT / path).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        errors.append(f"{path}: {exc}")
        return {}


def nested(obj, *keys):
    for key in keys:
        if not isinstance(obj, dict):
            return None
        obj = obj.get(key)
    return obj


def main():
    required = [
        "README.md", "LICENSE", ".mcp.json", "plugin.json", "kimi.plugin.json",
        "gemini-extension.json", "BROWSERPAIR.md", ".grok-plugin/plugin.json",
        ".cursor-plugin/marketplace.json", "skills/browserpair/SKILL.md",
        "plugins/browserpair/.cursor-plugin/plugin.json", "plugins/browserpair/mcp.json",
        "plugins/browserpair/skills/browserpair/SKILL.md",
        "plugins/browserpair/rules/browserpair.mdc", "plugins/browserpair/assets/logo.svg",
        "docs/connection-and-testing.md", "docs/gemini.md", "docs/grok.md",
        "docs/kimi.md", "docs/manus.md", "docs/mistral.md", "docs/perplexity.md",
    ]
    for rel in required:
        check((ROOT / rel).is_file(), f"Missing required package file: {rel}")

    manifests = {}
    for path in sorted(ROOT.rglob("*.json")):
        rel = path.relative_to(ROOT).as_posix()
        manifests[rel] = get_json(rel)

    core = manifests.get("plugin.json", {})
    check(core.get("name") == "browserpair", "Portable plugin name changed")
    check(core.get("repository") == "https://github.com/BrowserPair/browserpair-integrations", "Portable plugin repository changed")

    root_mcp = manifests.get(".mcp.json", {})
    check(nested(root_mcp, "mcpServers", "browserpair", "type") == "http", "Root MCP transport must be http")
    check(nested(root_mcp, "mcpServers", "browserpair", "url") in MCP_URLS, "Root MCP endpoint changed")

    kimi = manifests.get("kimi.plugin.json", {})
    check(nested(kimi, "mcpServers", "browserpair", "url") in MCP_URLS, "Kimi MCP endpoint changed")
    check((ROOT / str(kimi.get("skills", "__missing__"))).is_dir(), "Kimi skill directory missing")

    gemini = manifests.get("gemini-extension.json", {})
    check(nested(gemini, "mcpServers", "browserpair", "httpUrl") in MCP_URLS, "Gemini MCP endpoint changed")
    check((ROOT / str(gemini.get("contextFileName", "__missing__"))).is_file(), "Gemini context file missing")

    grok = manifests.get(".grok-plugin/plugin.json", {})
    check((ROOT / str(grok.get("skills", "__missing__"))).is_dir(), "Grok skills path missing")

    cursor = manifests.get(".cursor-plugin/marketplace.json", {})
    packages = cursor.get("plugins", [])
    check(isinstance(packages, list) and len(packages) > 0, "Cursor marketplace has no plugins")
    for package in packages if isinstance(packages, list) else []:
        source = str(package.get("source", "__missing__"))
        check((ROOT / source).is_dir(), f"Cursor plugin source missing: {source}")

    cursor_plugin = manifests.get("plugins/browserpair/.cursor-plugin/plugin.json", {})
    check(cursor_plugin.get("name") == "browserpair", "Cursor plugin name changed")
    logo = str(cursor_plugin.get("logo", "__missing__"))
    check((ROOT / "plugins/browserpair" / logo).is_file(), "Cursor plugin logo missing")
    cursor_mcp = manifests.get("plugins/browserpair/mcp.json", {})
    check(nested(cursor_mcp, "mcpServers", "browserpair", "url") in MCP_URLS, "Cursor MCP endpoint changed")

    for rel in ("plugin.json", "kimi.plugin.json", "gemini-extension.json",
                ".grok-plugin/plugin.json", "plugins/browserpair/.cursor-plugin/plugin.json"):
        version = manifests.get(rel, {}).get("version", "")
        check(bool(re.fullmatch(r"\d+\.\d+\.\d+", str(version))), f"Invalid version in {rel}")

    first = ROOT / "skills/browserpair/SKILL.md"
    second = ROOT / "plugins/browserpair/skills/browserpair/SKILL.md"
    if first.is_file() and second.is_file():
        check(first.read_bytes() == second.read_bytes(), "The two packaged BrowserPair Skills must stay identical")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    check(PLUGIN_URL in readme, "README missing published ChatGPT plugin")
    check(REGISTRY_URL in readme, "README missing GitHub MCP Registry listing")
    for page in ("connection-and-testing", "gemini", "grok", "kimi", "manus", "mistral", "perplexity"):
        check(f"docs/{page}.md" in readme, f"README missing documentation link: {page}")

    if errors:
        for err in errors:
            print(f"FAIL: {err}")
        raise SystemExit(1)
    print(f"PASS: {len(manifests)} JSON manifests, {len(required)} package files, MCP URLs, client paths, Skills, and public links")


if __name__ == "__main__":
    main()

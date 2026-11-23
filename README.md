<p align="center"><img src="https://browserpair.com/mark.svg" width="72" alt="BrowserPair logo"></p>

# BrowserPair integrations

Connect AI agents to **your own signed-in Chrome** using [BrowserPair](https://browserpair.com). BrowserPair provides a hosted remote MCP server, OAuth sign-in, browser permissions and verified task results. This repository contains **public client integration packages and setup guides**, not the private BrowserPair application source.

[**GitHub MCP Registry**](https://github.com/mcp/com.browserpair/browserpair) · [**ChatGPT plugin**](https://chatgpt.com/plugins/plugin_asdk_app_6ac5859a310c8191b959b4cfd69b2668) · [Chrome extension](https://chromewebstore.google.com/detail/agdomhjeahcbelohnmjmbldeldclnoof) · [Documentation](https://docs.browserpair.com/) · [BrowserPair app](https://app.browserpair.com/)

## Get started

1. Install the [Chrome extension](https://chromewebstore.google.com/detail/agdomhjeahcbelohnmjmbldeldclnoof) and pair the Chrome profile you want to use in the [BrowserPair app](https://app.browserpair.com/).
2. Choose your client below. In ChatGPT, open the published plugin and select **Connect**; other MCP clients can use their own OAuth connection setup.
3. Sign in to BrowserPair, review the requesting client and browser, and approve the connection. Then run the [read-only acceptance test](docs/connection-and-testing.md).

## Published listings

| Listing | Link | Status |
| --- | --- | --- |
| GitHub MCP Registry | [BrowserPair MCP server](https://github.com/mcp/com.browserpair/browserpair) | Listed; links to this repository as its integration source |
| ChatGPT | [Published BrowserPair plugin](https://chatgpt.com/plugins/plugin_asdk_app_6ac5859a310c8191b959b4cfd69b2668) | Published; connect using OAuth, without manually adding an MCP server |

An approved Registry listing, a published ChatGPT plugin and a client's personal MCP connection are **different distribution channels**. The Registry entry does not install the Chrome extension or authorize your browser. Registry preview pages may lag behind the latest README in this repository.

## Other client packages and connection guides

| Client | Installation or guide | Availability |
| --- | --- | --- |
| Cursor | [`plugins/browserpair/`](plugins/browserpair/) | Package available here; Cursor Marketplace listing not independently verified |
| Gemini / Gemini CLI | [Gemini guide](docs/gemini.md) · `gemini-extension.json` | CLI package available; consumer app directory approval not verified |
| Kimi / Kimi Code | [Kimi guide](docs/kimi.md) · `kimi.plugin.json` | Personal/CLI package available; official directory approval not verified |
| Grok / Grok Build | [Grok guide](docs/grok.md) · `.grok-plugin/` | Package available; official directory approval not verified |
| Perplexity | [Perplexity guide](docs/perplexity.md) · `plugin.json` | Custom import instructions; directory approval not verified |
| Mistral Le Chat / Vibe | [Mistral guide](docs/mistral.md) | Custom MCP connection instructions; directory approval not verified |
| Manus | [Manus guide](docs/manus.md) | Custom MCP connection instructions; directory approval not verified |

A package existing here is **not** proof of an external marketplace listing or an end-to-end OAuth test. Check the linked guide and the client's current capabilities before installing.

## Connect a generic MCP client

BrowserPair's remote MCP server supports OAuth. For a client that accepts an `mcpServers` configuration like the one in this repository's root `.mcp.json`:

```json
{
  "mcpServers": {
    "browserpair": {
      "type": "http",
      "url": "https://mcp.browserpair.com/mcp"
    }
  }
}
```

Some clients use the base URL `https://mcp.browserpair.com` instead. Use the endpoint and configuration expected by your particular client; these formats are not interchangeable across all apps. For full instructions see [Remote MCP documentation](https://docs.browserpair.com/remote-mcp) and the [connection test](docs/connection-and-testing.md).

## Repository layout

| Path | Purpose |
| --- | --- |
| `plugin.json`, `.mcp.json`, `skills/` | Portable root plugin and remote MCP configuration (used by importers such as Perplexity) |
| `gemini-extension.json`, `BROWSERPAIR.md` | Gemini CLI integration and context |
| `kimi.plugin.json`, `.grok-plugin/` | Kimi and Grok Build package metadata |
| `.cursor-plugin/`, `plugins/browserpair/` | Cursor marketplace entry and bundled plugin |
| `docs/` | Platform-specific guides and the shared acceptance test |
| `scripts/validate_integrations.py` | Offline manifest, path and Skill-consistency checks |

Some files deliberately appear in more than one package: `skills/browserpair/SKILL.md` and `plugins/browserpair/skills/browserpair/SKILL.md` must stay identical. **Do not move or delete root manifests or plugin directories** without validating each client's installation format. These paths are part of the distributable packages.

## Contribute and verify

Run `python3 scripts/validate_integrations.py` before submitting changes. GitHub Actions runs the same check on pull requests and updates to `main`. The script validates JSON, referenced package files, MCP endpoint formats, both Skill copies and documentation links. It cannot prove live OAuth compatibility or marketplace publication: test those separately with the [acceptance checklist](docs/connection-and-testing.md).

**Privacy and safety:** The connected Chrome profile keeps its signed-in sessions; browser observations and results can reach the connected AI app. Respect BrowserPair Permissions, confirmations and website policies. Never commit credentials, cookies or user data. [Security](https://browserpair.com/security) · [Privacy](https://browserpair.com/privacy) · [Support](https://browserpair.com/support) · [Product hub](https://github.com/BrowserPair/browserpair)

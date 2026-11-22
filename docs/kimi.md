# Kimi

## Kimi web / Work

Open [Plugins](https://www.kimi.ai/plugins), check Personal and Installed for an existing BrowserPair plugin, and choose Custom plugin. Give Plugin Builder this public repository URL and the MCP URL `https://mcp.browserpair.com`. Ask it to use `kimi.plugin.json` and the existing BrowserPair skill, register the actual personal plugin, then install and complete OAuth.

Run the [acceptance test](connection-and-testing.md) before claiming compatibility. From the tested personal plugin's details, choose the envelope/feedback button and “Apply for official marketplace publication”; provide your contact email. This is an application for review, not immediate public publication.

## Kimi Code

This repository contains the root `kimi.plugin.json` manifest and uses only a remote OAuth MCP server plus a declarative skill. In Kimi Code:

```text
/plugins install https://github.com/BrowserPair/browserpair-integrations
/reload
```

Complete the BrowserPair authorization when prompted; never enter an API key in the manifest.

Sources: [Plugin format and installation](https://www.kimi.com/code/docs/en/kimi-code-cli/customization/plugins.html), [Personal plugins](https://www.kimi.com/en/help/plugins-and-skills/create), [Marketplace publication](https://www.kimi.com/en/help/plugins-and-skills/publish).

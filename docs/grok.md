# Grok, Grok Bot and Grok Build

## Grok custom MCP

Open [Connect Apps](https://grok.com/connectors), check Your apps for BrowserPair, then choose Add a custom connector. Name it BrowserPair and enter `https://mcp.browserpair.com`. Leave static headers empty and complete BrowserPair OAuth if offered. Run the [acceptance test](connection-and-testing.md). Availability can depend on the account and product.

## Grok Bot directory

The [official submission form](https://x.ai/bot/marketplace/submit-a-plugin) accepts a remote MCP URL or public repository. It requires a logo with a background plate, testing instructions, a truthful local and in-app test attestation, and acceptance of Publisher Terms. Do not attest to a test that has not run. Its Grok listing option is labelled coming soon. A form submission does not publish a Grok Build catalog entry.

## Grok Build

This repository contains `.grok-plugin/plugin.json`, `.mcp.json` and a referenced BrowserPair skill. The remote MCP is Streamable HTTP with OAuth; no local executable or hook is included. Follow your current Grok Build plugin installer, then complete OAuth and run the acceptance test.

The [official Build catalog](https://github.com/xai-org/plugin-marketplace) accepts pull requests to `.grok-plugin/marketplace.json`. Reference this public repository and pin a full 40-character commit SHA. Regenerate the component index and run the catalog validator. Catalog review and approval are separate from publishing these source files.

Sources: [Connectors](https://docs.x.ai/grok/connectors), [Build plugin support](https://docs.x.ai/build/features/skills-plugins-marketplaces), [Catalog contribution guide](https://github.com/xai-org/plugin-marketplace/blob/main/CONTRIBUTING.md).

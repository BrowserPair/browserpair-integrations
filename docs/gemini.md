# Google Gemini

## Gemini app and Search

The [Connected Apps Platform](https://developers.google.com/connected-apps/) offers a preview registration and review path for cloud-hosted MCP services. Use [Google Connected Console](https://connected.google.com/console/) to check eligibility and preview access. Review the [MCP guide](https://developers.google.com/connected-apps/mcp) and [registration steps](https://developers.google.com/connected-apps/gpc/perform-the-steps) before configuring a listing. Use the existing BrowserPair MCP server and OAuth; do not invent an Android app, company identity or supported region.

A preview application, developer-mode test and public approved app are separate statuses. Google may require ownership verification and policy checks. Production security or OAuth changes need an independent review.

## Gemini CLI

This repository provides `gemini-extension.json` at the root and `BROWSERPAIR.md` guidance. Install with:

```sh
gemini extensions install https://github.com/BrowserPair/browserpair-integrations
```

The extension uses `httpUrl` for Streamable HTTP and no embedded credential. Complete OAuth through the client, then run the [acceptance test](connection-and-testing.md). A successful CLI install is not an authenticated browser test and does not list BrowserPair inside the Gemini consumer app.

The [CLI gallery](https://geminicli.com/docs/extensions/releasing/) discovers public repositories with the `gemini-cli-extension` topic and a root manifest, crawls daily and validates them. Adding the topic is a discovery request, not proof of gallery visibility.

The official [preview interest form](https://connected.google.com/console/help/?apply=) routes existing Play Developer account administrators to the matching Play Console form. An access request joins a waitlist; it does not register or publish an approved consumer app.

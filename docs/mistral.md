# Mistral Le Chat / Vibe

Open the app's Connectors settings, inspect existing connections, and add a Custom MCP connector:

- Name: BrowserPair
- Server: `https://mcp.browserpair.com`
- Authentication: OAuth 2.1
- Description: Work in your own signed-in Chrome with BrowserPair.

Complete BrowserPair authorization and run the [acceptance test](connection-and-testing.md). Choose a private connection for a personal test; do not grant organization-wide access just to test.

[Studio connector management](https://docs.mistral.ai/studio/connectors/management) supports private, workspace and organization scopes. Sharing inside a workspace is not a public directory listing. Directory publication is subject to separate [Connector Terms](https://legal.mistral.ai/terms/connectors-terms/) and review; this package does not claim approval.

Sources: [Connectors overview](https://docs.mistral.ai/studio/connectors/overview), [Mistral announcement](https://mistral.ai/news/connectors/).

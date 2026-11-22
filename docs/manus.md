# Manus

Open Connectors, check for an existing BrowserPair entry, and choose Create → Add MCP by URL. Enter BrowserPair and `https://mcp.browserpair.com`. Complete OAuth if prompted. Manus also documents JSON import; the shared remote MCP configuration uses:

```json
{"mcpServers":{"browserpair":{"url":"https://mcp.browserpair.com"}}}
```

Run the [acceptance test](connection-and-testing.md) using the actual BrowserPair tools. Manus has its own browser tool: a task completed with that browser does not prove the BrowserPair connection works.

Publishing a connector to a Manus Project shares a project capability and is not proof of admission to the global connector catalog.

Sources: [Official connectors guide](https://www.manus.im/features/connectors), [Help center](https://help.manus.im/en/articles/12231777-how-can-i-use-manus-connectors).

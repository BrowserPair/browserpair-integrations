<p align="center"><img src="https://browserpair.com/mark.svg" width="72" alt="BrowserPair logo"></p>

# BrowserPair integrations

Official, open-source integration packages that connect AI coding tools and agents to [BrowserPair](https://browserpair.com), the hosted MCP server that lets agents work in your own signed-in Chrome.

| Integration | Path | Status |
| --- | --- | --- |
| Cursor plugin | [`plugins/browserpair`](plugins/browserpair) | Plugin package in this repository (Marketplace listing not independently verified) |
| Remote MCP (any MCP client) | `https://mcp.browserpair.com` (OAuth) | Listed in the [official MCP Registry](https://registry.modelcontextprotocol.io/v0.1/servers/com.browserpair%2Fbrowserpair/versions/latest) as `com.browserpair/browserpair` |

These packages contain only connection metadata, skills and rules. BrowserPair's application and extension source code are private and maintained separately.

## Use BrowserPair from any MCP client

Add a remote MCP server with the URL `https://mcp.browserpair.com` and sign in with your BrowserPair account when the client asks (OAuth 2.1 with PKCE). For example, in a client that reads `mcp.json`:

```json
{
  "mcpServers": {
    "browserpair": {
      "url": "https://mcp.browserpair.com"
    }
  }
}
```

You also need the [BrowserPair Chrome extension](https://chromewebstore.google.com/detail/agdomhjeahcbelohnmjmbldeldclnoof) connected to your account. See the [Remote MCP documentation](https://docs.browserpair.com/remote-mcp).

## Links

[Website](https://browserpair.com) · [Documentation](https://docs.browserpair.com/) · [Product hub](https://github.com/BrowserPair/browserpair) · [Support](https://browserpair.com/support) · [Security](https://browserpair.com/security)

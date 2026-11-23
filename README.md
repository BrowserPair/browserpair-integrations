<p align="center"><img src="https://browserpair.com/mark.svg" width="72" alt="BrowserPair logo"></p>

# BrowserPair integrations

Official, open-source integration packages that connect AI coding tools and agents to [BrowserPair](https://browserpair.com), the hosted MCP server that lets agents work in your own signed-in Chrome.

| Integration | Path | Status |
| --- | --- | --- |
| ChatGPT | [Published BrowserPair plugin](https://chatgpt.com/plugins/plugin_asdk_app_6ac5859a310c8191b959b4cfd69b2668) | Published in ChatGPT; select **Connect** and authorize your browser |
| Cursor plugin | [`plugins/browserpair`](plugins/browserpair) | Plugin package in this repository (Marketplace listing not independently verified) |
| Remote MCP (any MCP client) | `https://mcp.browserpair.com` (OAuth) | Listed in the [official MCP Registry](https://registry.modelcontextprotocol.io/v0.1/servers/com.browserpair%2Fbrowserpair/versions/latest) as `com.browserpair/browserpair` |
| Kimi | [`docs/kimi.md`](docs/kimi.md) | Public connection package; live acceptance and directory review tracked separately |
| Grok / Grok Bot / Grok Build | [`docs/grok.md`](docs/grok.md) | Public connection package; live acceptance and directory review tracked separately |
| Perplexity | [`docs/perplexity.md`](docs/perplexity.md) | Public connection package; live acceptance and directory review tracked separately |
| Mistral Le Chat / Vibe | [`docs/mistral.md`](docs/mistral.md) | Public connection package; live acceptance and directory review tracked separately |
| Manus | [`docs/manus.md`](docs/manus.md) | Public connection package; live acceptance and directory review tracked separately |
| Gemini / Gemini CLI | [`docs/gemini.md`](docs/gemini.md) | Public connection package; live acceptance and directory review tracked separately |

These packages contain only connection metadata, skills and rules. BrowserPair's application and extension source code are private and maintained separately.

## Connect BrowserPair in ChatGPT

Open the [published BrowserPair plugin](https://chatgpt.com/plugins/plugin_asdk_app_6ac5859a310c8191b959b4cfd69b2668) in ChatGPT and select **Connect**. Sign in to BrowserPair and choose which connected Chrome browser to authorize. The published plugin uses OAuth; you do **not** need to add a custom MCP server or enable ChatGPT Developer mode for this setup. See the [ChatGPT guide](https://docs.browserpair.com/chatgpt).

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

## Verify a connection

Follow [connection, permissions and acceptance](docs/connection-and-testing.md). Platform-specific metadata contains no credentials, app source or production configuration. Publishing this repository does not by itself submit or approve a marketplace listing.

The root `plugin.json` and `skills/` also expose a portable Agent Plugins package. Perplexity can import the repository from its Add custom menu, subject to account eligibility. See the [Perplexity guide](docs/perplexity.md).

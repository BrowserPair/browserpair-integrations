# Perplexity

Open Perplexity Plugins (or Connectors on older layouts), check for an existing BrowserPair connector, and choose Add custom → MCP connector → Remote. Use:

- Name: BrowserPair
- Server: `https://mcp.browserpair.com`
- Transport: Streamable HTTP
- Authentication: OAuth

Complete BrowserPair OAuth and run the [acceptance test](connection-and-testing.md). The [March 2026 announcement](https://www.perplexity.ai/changelog/what-we-shipped---march-13-2026) describes custom remote connectors for Pro, Max and Enterprise; check current account availability before buying anything.

The [connector submission form](https://pplx.ai/connector-form-submission) is separate from a personal connection. It asks for company and legal entity information. Submit only truthful authorized information; an individual should not invent a registered company or tax identity.

This guide and the shared remote MCP configuration are public connection materials. They do not establish a Perplexity directory listing or a completed in-app test.

## Import the public plugin

On [Plugins](https://www.perplexity.ai/computer/plugins), choose Add custom → Import plugin from GitHub and enter `https://github.com/BrowserPair/browserpair-integrations`. The root `plugin.json`, root skill directory and `.mcp.json` provide the portable package. Confirm that BrowserPair appears as a connector; an imported skill alone does not establish the connection. Complete OAuth for that connector if your plan allows it.

[Current package requirements](https://www.perplexity.ai/help-center/en/articles/2026100802-create-or-upload-a-custom-plugin) require remote MCP servers to declare a type, which this package sets to `http`. Skills need a plan that includes Computer. A public GitHub package is shareable, while the imported personal copy remains private to your account.

For clients that derive the OAuth resource from the server URL, use `https://mcp.browserpair.com/mcp` as declared by this package. The explicit `/mcp` endpoint avoids a root-URL trailing-slash mismatch while preserving the server’s resource validation.

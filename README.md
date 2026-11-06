# Intellier Trifecta Marketplace

Private plugin marketplace that delivers **Trifecta Marketing OS** to everyone in Julie Warnock's Claude organization (Bath Promotions, Custom Candles LA, Julie Warnock founder brand).

Maintained by Intellier AI Technologies. Members can use the plugin but not edit it; all changes go through this repo.

## Layout

```
.claude-plugin/marketplace.json      marketplace manifest (lists the plugins)
plugins/trifecta-marketing-os/       the plugin itself (skills, agents, .mcp.json)
```

## Connect it to Julie's org (one time)

1. In Julie's Claude account (Owner role): **Organization settings > Plugins & skills > Marketplaces**.
2. Add plugins, source **GitHub**, repo `jlh210/trifecta-marketplace`. Approve the Claude GitHub App for this repo if prompted.
3. Set **Trifecta Marketing OS** to **Required**.
4. In **Organization settings > Connectors**, add the connectors the plugin uses (GoHighLevel, Metricool, Klaviyo, Google Sheets/Drive, GA4/Search Console, Higgsfield, Canva). Each member connects with their own login.
5. Run `marketing-routines-setup` once, on the approver's account only.

## Ship an update

1. Edit files under `plugins/trifecta-marketing-os/`.
2. Bump `version` in **both** `plugins/trifecta-marketing-os/.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`.
3. Validate: `claude plugin validate .`
4. Commit and push to `main`.
5. In Julie's org: **Plugins & skills > Marketplaces > Re-sync**.

## Claude Code install

```
/plugin install trifecta-marketing-os --marketplace jlh210/trifecta-marketplace
```

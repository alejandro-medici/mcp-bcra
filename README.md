# mcp-bcra

MCP server for Argentina's Central Bank (BCRA) APIs. Enables AI agents to access financial data including exchange rates, monetary variables, debtor registry, and more.

## Available Tools

| Tool | Description |
|------|-------------|
| `bcra_variables_principales` | Current values of key monetary variables (reserves, exchange rate, inflation, etc.) |
| `bcra_variable_historico` | Historical series for a variable by ID and date range |
| `bcra_tipos_de_cambio` | List of available exchange rate types |
| `bcra_cotizacion` | Currency quotations for a given date |
| `bcra_deudores` | Current credit situation of a person or company |
| `bcra_deudores_historico` | Credit history of a person or company |
| `bcra_entidades_cheques` | List of financial entities for check queries |
| `bcra_cheques_rechazados` | Rejected checks by CUIT |
| `bcra_cheque_por_numero` | Look up a specific check by entity and number |
| `bcra_entidades_financieras` | List of financial entities (transparency regime) |
| `bcra_tasas` | Active and passive rates by financial entity |

## Requirements

- Python 3.13+
- [Dev Container](https://containers.dev/) (recommended)

## Installation

```bash
pip install mcp-bcra
```

Or run directly with `uvx`:

```bash
uvx mcp-bcra
```

## Usage with Claude

Add to your MCP client configuration:

```json
{
  "mcpServers": {
    "bcra": {
      "command": "uvx",
      "args": ["mcp-bcra"]
    }
  }
}
```

## Development

Open in VSCode with the Dev Container extension — the environment is fully configured.

```bash
pip install -e ".[dev]"
pytest
```

## Data Source

All data comes from the [BCRA public APIs](https://www.bcra.gob.ar/apis-banco-central/).

## License

MIT

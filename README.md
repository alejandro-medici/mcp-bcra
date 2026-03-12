# mcp-bcra

MCP server for Argentina's Central Bank (BCRA) public APIs. Enables AI agents to access financial data including exchange rates, monetary variables, debtor registry, transparency regime, and more.

## Available Tools

### Variables Monetarias
| Tool | Description |
|------|-------------|
| `bcra_variables` | List monetary variables published by the BCRA (reserves, exchange rate, inflation, etc.) |
| `bcra_variable_historico` | Historical series for a monetary variable by ID and date range |

### Estadísticas Cambiarias
| Tool | Description |
|------|-------------|
| `bcra_divisas` | List all active ISO currencies with their denomination |
| `bcra_cotizaciones` | Currency quotations published by the BCRA for a given date |
| `bcra_evolucion_moneda` | Exchange rate evolution for a currency over a date range |

### Central de Deudores
| Tool | Description |
|------|-------------|
| `bcra_deudores` | Current credit situation of a person or company (debt, days overdue, status per entity) |
| `bcra_deudores_historico` | Credit history for the last 24 months |
| `bcra_cheques_rechazados` | Rejected checks and their reasons for a given CUIT/CUIL/CDI |

### Cheques Denunciados
| Tool | Description |
|------|-------------|
| `bcra_entidades_cheques` | List all banking entities with their entity codes |
| `bcra_cheque` | Check if a specific check is registered as reported |

### Régimen de Transparencia
| Tool | Description |
|------|-------------|
| `bcra_cajas_ahorro` | Savings accounts offered by financial entities |
| `bcra_paquetes_productos` | Product packages offered by financial entities |
| `bcra_plazos_fijos` | Fixed-term deposit rates and conditions |
| `bcra_prestamos_prendarios` | Pledge loan rates and conditions |
| `bcra_prestamos_hipotecarios` | Mortgage loan rates and conditions |
| `bcra_prestamos_personales` | Personal loan rates and conditions |
| `bcra_tarjetas_credito` | Credit card rates and conditions |

## Installation

```bash
pip install mcp-bcra
```

Or run directly without installing via `uvx`:

```bash
uvx mcp-bcra
```

## Usage with MCP clients

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

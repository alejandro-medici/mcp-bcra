from bcra_mcp.client import get


async def get_tipos_de_cambio() -> dict:
    """Lista todos los tipos de cambio disponibles."""
    return await get("/estadisticascambiarias/v1.0/Maestros/TiposDeCambio")


async def get_cotizacion(fecha: str, tipo_cambio: str = "BNA") -> dict:
    """
    Retorna la cotización de todas las monedas para una fecha dada.

    Args:
        fecha: Fecha en formato YYYY-MM-DD
        tipo_cambio: Código del tipo de cambio (default: BNA - Banco Nación Argentina)
    """
    return await get(f"/estadisticascambiarias/v1.0/Cotizaciones/{tipo_cambio}/{fecha}")

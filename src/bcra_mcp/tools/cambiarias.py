from bcra_mcp.client import get


async def get_divisas() -> dict:
    """Lista todas las monedas ISO vigentes con su denominación."""
    return await get("/estadisticascambiarias/v1.0/Maestros/Divisas")


async def get_cotizaciones(fecha: str | None = None) -> dict:
    """Retorna todas las cotizaciones de divisas publicadas por el BCRA para una fecha.
    Si no se ingresa fecha, devuelve la última cotización disponible.

    Args:
        fecha: Fecha en formato YYYY-MM-DD (opcional)
    """
    params = {}
    if fecha:
        params["fecha"] = fecha
    return await get("/estadisticascambiarias/v1.0/Cotizaciones", params=params)


async def get_evolucion_moneda(
    moneda: str,
    fechadesde: str | None = None,
    fechahasta: str | None = None,
    limit: int = 1000,
    offset: int = 0,
) -> dict:
    """Retorna la evolución de cotización de una moneda ISO en un rango de fechas.

    Args:
        moneda: Código ISO de la moneda (ej: "USD", "EUR", "BRL")
        fechadesde: Fecha de inicio en formato YYYY-MM-DD (opcional)
        fechahasta: Fecha de fin en formato YYYY-MM-DD (opcional)
        limit: Cantidad máxima de registros, entre 10 y 1000
        offset: Registros a descartar para paginado
    """
    params: dict = {"limit": limit, "offset": offset}
    if fechadesde:
        params["fechaDesde"] = fechadesde
    if fechahasta:
        params["fechaHasta"] = fechahasta
    return await get(f"/estadisticascambiarias/v1.0/Cotizaciones/{moneda}", params=params)

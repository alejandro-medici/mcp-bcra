from bcra_mcp.client import get


async def get_variables(
    id_variable: int | None = None,
    categoria: str | None = None,
    periodicidad: str | None = None,
    offset: int = 0,
    limit: int = 1000,
) -> dict:
    """Lista las variables monetarias publicadas por el BCRA.

    Args:
        id_variable: Filtra por ID de variable
        categoria: Filtra por categoría (ej: "Principales Variables")
        periodicidad: D (diaria), M (mensual), T/Q (trimestral)
        offset: Registros a descartar para paginado
        limit: Cantidad máxima de registros (max 1000)
    """
    params: dict = {"Offset": offset, "Limit": limit}
    if id_variable is not None:
        params["IdVariable"] = id_variable
    if categoria:
        params["Categoria"] = categoria
    if periodicidad:
        params["Periodicidad"] = periodicidad
    return await get("/estadisticas/v4.0/Monetarias", params=params)


async def get_variable_historico(
    id_variable: int,
    desde: str | None = None,
    hasta: str | None = None,
    offset: int = 0,
    limit: int = 1000,
) -> dict:
    """Retorna la evolución de valores de una variable monetaria en un rango de fechas.

    Args:
        id_variable: ID de la variable (obtenido de get_variables)
        desde: Fecha de inicio en formato YYYY-MM-DD (default: primera fecha de la serie)
        hasta: Fecha de fin en formato YYYY-MM-DD (default: última fecha de la serie)
        offset: Registros a descartar para paginado
        limit: Cantidad máxima de registros (max 3000)
    """
    params: dict = {"Offset": offset, "Limit": limit}
    if desde:
        params["Desde"] = desde
    if hasta:
        params["Hasta"] = hasta
    return await get(f"/estadisticas/v4.0/Monetarias/{id_variable}", params=params)

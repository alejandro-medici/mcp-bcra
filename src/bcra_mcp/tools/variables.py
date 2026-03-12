from bcra_mcp.client import get


async def get_principales_variables() -> dict:
    """Lista todas las variables monetarias principales con su valor actual."""
    return await get("/estadisticasmonetarias/v2.0/PrincipalesVariables")


async def get_variable_historico(id_variable: int, desde: str, hasta: str) -> dict:
    """
    Retorna la serie histórica de una variable monetaria.

    Args:
        id_variable: ID de la variable (obtenido de get_principales_variables)
        desde: Fecha inicio en formato YYYY-MM-DD
        hasta: Fecha fin en formato YYYY-MM-DD
    """
    return await get(f"/estadisticasmonetarias/v2.0/DatosVariable/{id_variable}/{desde}/{hasta}")

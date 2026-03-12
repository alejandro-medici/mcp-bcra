from bcra_mcp.client import get


async def get_entidades_financieras() -> dict:
    """Lista todas las entidades financieras del régimen de transparencia."""
    return await get("/transparencia/v1.0/entidades")


async def get_tasas(codigo_entidad: int) -> dict:
    """
    Retorna las tasas activas y pasivas de una entidad financiera.

    Args:
        codigo_entidad: Código de la entidad (obtenido de get_entidades_financieras)
    """
    return await get(f"/transparencia/v1.0/tasas/{codigo_entidad}")

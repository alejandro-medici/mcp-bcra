from bcra_mcp.client import get


async def get_entidades() -> dict:
    """Lista todas las entidades bancarias del país con su código de entidad."""
    return await get("/cheques/v1.0/entidades")


async def get_cheque(codigo_entidad: int, numero_cheque: int) -> dict:
    """Consulta si un cheque de una entidad está registrado como denunciado.

    Args:
        codigo_entidad: Código de la entidad bancaria (obtenido de get_entidades)
        numero_cheque: Número del cheque a consultar
    """
    return await get(f"/cheques/v1.0/denunciados/{codigo_entidad}/{numero_cheque}")

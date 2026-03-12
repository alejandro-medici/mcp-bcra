from bcra_mcp.client import get


async def get_entidades() -> dict:
    """Lista todas las entidades financieras habilitadas."""
    return await get("/cheques/v1.0/entidades")


async def get_cheques_rechazados(cuit: str) -> dict:
    """
    Retorna los cheques rechazados asociados a un CUIT.

    Args:
        cuit: CUIT de la persona o empresa (sin guiones ni espacios)
    """
    return await get(f"/cheques/v1.0/denunciados/{cuit}/0")


async def get_cheque_por_numero(
    codigo_entidad: int, numero_cheque: int, denunciado: bool = False
) -> dict:
    """
    Busca un cheque por entidad y número.

    Args:
        codigo_entidad: Código de la entidad bancaria
        numero_cheque: Número del cheque
        denunciado: True para cheques denunciados, False para rechazados
    """
    tipo = 1 if denunciado else 0
    return await get(f"/cheques/v1.0/denunciados/{codigo_entidad}/{numero_cheque}/{tipo}")

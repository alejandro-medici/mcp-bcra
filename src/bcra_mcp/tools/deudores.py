from bcra_mcp.client import get


async def get_deudores(identificacion: str) -> dict:
    """Retorna la situación crediticia actual de una persona o empresa.
    Incluye monto de deuda, días de atraso y situación por entidad financiera.

    Args:
        identificacion: CUIT/CUIL/CDI de 11 dígitos sin guiones ni espacios
    """
    return await get(f"/CentralDeDeudores/v1.0/Deudas/{identificacion}")


async def get_deudores_historico(identificacion: str) -> dict:
    """Retorna el historial crediticio de los últimos 24 meses de una persona o empresa.

    Args:
        identificacion: CUIT/CUIL/CDI de 11 dígitos sin guiones ni espacios
    """
    return await get(f"/CentralDeDeudores/v1.0/Deudas/Historicas/{identificacion}")


async def get_cheques_rechazados(identificacion: str) -> dict:
    """Retorna los cheques rechazados con sus causales para un CUIT/CUIL/CDI.

    Args:
        identificacion: CUIT/CUIL/CDI de 11 dígitos sin guiones ni espacios
    """
    return await get(f"/CentralDeDeudores/v1.0/Deudas/ChequesRechazados/{identificacion}")

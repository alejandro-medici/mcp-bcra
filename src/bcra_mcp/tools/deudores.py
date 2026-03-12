from bcra_mcp.client import get


async def get_deudores(identificacion: str) -> dict:
    """
    Retorna la situación crediticia actual de una persona o empresa.

    Args:
        identificacion: CUIT/CUIL/DNI del deudor (sin guiones ni espacios)
    """
    return await get(f"/centraldedeudores/v1.0/Deudas/{identificacion}")


async def get_deudores_historico(identificacion: str) -> dict:
    """
    Retorna el historial crediticio de una persona o empresa.

    Args:
        identificacion: CUIT/CUIL/DNI del deudor (sin guiones ni espacios)
    """
    return await get(f"/centraldedeudores/v1.0/Deudas/Historicas/{identificacion}")

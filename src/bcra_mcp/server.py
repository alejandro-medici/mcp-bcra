import asyncio
from mcp.server.fastmcp import FastMCP

from bcra_mcp.tools import variables, cambiarias, deudores, cheques, transparencia

mcp = FastMCP("mcp-bcra")


# --- Variables Monetarias ---

@mcp.tool()
async def bcra_variables_principales() -> str:
    """Lista todas las variables monetarias clave del BCRA con su valor actual.
    Incluye: reservas internacionales, base monetaria, tipo de cambio oficial, inflación, entre otras."""
    result = await variables.get_principales_variables()
    return str(result)


@mcp.tool()
async def bcra_variable_historico(id_variable: int, desde: str, hasta: str) -> str:
    """Retorna la serie histórica de una variable monetaria del BCRA.

    Args:
        id_variable: ID numérico de la variable (obtenido de bcra_variables_principales)
        desde: Fecha de inicio en formato YYYY-MM-DD
        hasta: Fecha de fin en formato YYYY-MM-DD
    """
    result = await variables.get_variable_historico(id_variable, desde, hasta)
    return str(result)


# --- Estadísticas Cambiarias ---

@mcp.tool()
async def bcra_tipos_de_cambio() -> str:
    """Lista todos los tipos de cambio disponibles en el BCRA (BNA, MEP, CCL, etc.)."""
    result = await cambiarias.get_tipos_de_cambio()
    return str(result)


@mcp.tool()
async def bcra_cotizacion(fecha: str, tipo_cambio: str = "BNA") -> str:
    """Retorna la cotización de todas las monedas para una fecha dada.

    Args:
        fecha: Fecha en formato YYYY-MM-DD
        tipo_cambio: Código del tipo de cambio (default: BNA - Banco Nación Argentina)
    """
    result = await cambiarias.get_cotizacion(fecha, tipo_cambio)
    return str(result)


# --- Central de Deudores ---

@mcp.tool()
async def bcra_deudores(identificacion: str) -> str:
    """Consulta la situación crediticia actual de una persona o empresa en el sistema financiero argentino.

    Args:
        identificacion: CUIT, CUIL o DNI sin guiones ni espacios
    """
    result = await deudores.get_deudores(identificacion)
    return str(result)


@mcp.tool()
async def bcra_deudores_historico(identificacion: str) -> str:
    """Consulta el historial crediticio de una persona o empresa.

    Args:
        identificacion: CUIT, CUIL o DNI sin guiones ni espacios
    """
    result = await deudores.get_deudores_historico(identificacion)
    return str(result)


# --- Cheques ---

@mcp.tool()
async def bcra_entidades_cheques() -> str:
    """Lista todas las entidades financieras habilitadas para consulta de cheques."""
    result = await cheques.get_entidades()
    return str(result)


@mcp.tool()
async def bcra_cheques_rechazados(cuit: str) -> str:
    """Consulta los cheques rechazados asociados a un CUIT.

    Args:
        cuit: CUIT de la persona o empresa sin guiones ni espacios
    """
    result = await cheques.get_cheques_rechazados(cuit)
    return str(result)


@mcp.tool()
async def bcra_cheque_por_numero(codigo_entidad: int, numero_cheque: int, denunciado: bool = False) -> str:
    """Busca un cheque específico por entidad y número.

    Args:
        codigo_entidad: Código numérico de la entidad bancaria
        numero_cheque: Número del cheque
        denunciado: True para cheques denunciados, False para rechazados (default: False)
    """
    result = await cheques.get_cheque_por_numero(codigo_entidad, numero_cheque, denunciado)
    return str(result)


# --- Régimen de Transparencia ---

@mcp.tool()
async def bcra_entidades_financieras() -> str:
    """Lista todas las entidades financieras del régimen de transparencia del BCRA."""
    result = await transparencia.get_entidades_financieras()
    return str(result)


@mcp.tool()
async def bcra_tasas(codigo_entidad: int) -> str:
    """Retorna las tasas activas y pasivas de una entidad financiera.

    Args:
        codigo_entidad: Código numérico de la entidad (obtenido de bcra_entidades_financieras)
    """
    result = await transparencia.get_tasas(codigo_entidad)
    return str(result)


def main():
    mcp.run()


if __name__ == "__main__":
    main()

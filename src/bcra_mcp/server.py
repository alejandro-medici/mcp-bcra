from mcp.server.fastmcp import FastMCP

from bcra_mcp.tools import cambiarias, cheques, deudores, transparencia, variables

mcp = FastMCP("mcp-bcra")


# --- Variables Monetarias ---


@mcp.tool()
async def bcra_variables(
    id_variable: int | None = None,
    categoria: str | None = None,
    periodicidad: str | None = None,
    offset: int = 0,
    limit: int = 1000,
) -> str:
    """Lista las variables monetarias publicadas por el BCRA.
    Incluye reservas internacionales, base monetaria, tipo de cambio, inflación y más.

    Args:
        id_variable: Filtra por ID de variable (opcional)
        categoria: Filtra por categoría, ej: "Principales Variables" (opcional)
        periodicidad: D (diaria), M (mensual), T/Q (trimestral) (opcional)
        offset: Registros a descartar para paginado
        limit: Cantidad máxima de registros (max 1000)
    """
    result = await variables.get_variables(id_variable, categoria, periodicidad, offset, limit)
    return str(result)


@mcp.tool()
async def bcra_variable_historico(
    id_variable: int,
    desde: str | None = None,
    hasta: str | None = None,
    offset: int = 0,
    limit: int = 1000,
) -> str:
    """Retorna la evolución histórica de una variable monetaria del BCRA.

    Args:
        id_variable: ID numérico de la variable (obtenido de bcra_variables)
        desde: Fecha de inicio en formato YYYY-MM-DD (opcional)
        hasta: Fecha de fin en formato YYYY-MM-DD (opcional)
        offset: Registros a descartar para paginado
        limit: Cantidad máxima de registros (max 3000)
    """
    result = await variables.get_variable_historico(id_variable, desde, hasta, offset, limit)
    return str(result)


# --- Estadísticas Cambiarias ---


@mcp.tool()
async def bcra_divisas() -> str:
    """Lista todas las monedas ISO vigentes con su denominación."""
    result = await cambiarias.get_divisas()
    return str(result)


@mcp.tool()
async def bcra_cotizaciones(fecha: str | None = None) -> str:
    """Retorna todas las cotizaciones de divisas publicadas por el BCRA.
    Si no se ingresa fecha, devuelve la última cotización disponible.

    Args:
        fecha: Fecha en formato YYYY-MM-DD (opcional)
    """
    result = await cambiarias.get_cotizaciones(fecha)
    return str(result)


@mcp.tool()
async def bcra_evolucion_moneda(
    moneda: str,
    fechadesde: str | None = None,
    fechahasta: str | None = None,
    limit: int = 1000,
    offset: int = 0,
) -> str:
    """Retorna la evolución de cotización de una moneda en un rango de fechas.

    Args:
        moneda: Código ISO de la moneda (ej: "USD", "EUR", "BRL")
        fechadesde: Fecha de inicio en formato YYYY-MM-DD (opcional)
        fechahasta: Fecha de fin en formato YYYY-MM-DD (opcional)
        limit: Cantidad máxima de registros, entre 10 y 1000
        offset: Registros a descartar para paginado
    """
    result = await cambiarias.get_evolucion_moneda(moneda, fechadesde, fechahasta, limit, offset)
    return str(result)


# --- Central de Deudores ---


@mcp.tool()
async def bcra_deudores(identificacion: str) -> str:
    """Consulta la situación crediticia actual de una persona o empresa.
    Incluye monto de deuda, días de atraso y situación por entidad financiera.

    Args:
        identificacion: CUIT/CUIL/CDI de 11 dígitos sin guiones ni espacios
    """
    result = await deudores.get_deudores(identificacion)
    return str(result)


@mcp.tool()
async def bcra_deudores_historico(identificacion: str) -> str:
    """Consulta el historial crediticio de los últimos 24 meses de una persona o empresa.

    Args:
        identificacion: CUIT/CUIL/CDI de 11 dígitos sin guiones ni espacios
    """
    result = await deudores.get_deudores_historico(identificacion)
    return str(result)


@mcp.tool()
async def bcra_cheques_rechazados(identificacion: str) -> str:
    """Consulta los cheques rechazados con sus causales para un CUIT/CUIL/CDI.

    Args:
        identificacion: CUIT/CUIL/CDI de 11 dígitos sin guiones ni espacios
    """
    result = await deudores.get_cheques_rechazados(identificacion)
    return str(result)


# --- Cheques Denunciados ---


@mcp.tool()
async def bcra_entidades_cheques() -> str:
    """Lista todas las entidades bancarias del país con su código de entidad."""
    result = await cheques.get_entidades()
    return str(result)


@mcp.tool()
async def bcra_cheque(codigo_entidad: int, numero_cheque: int) -> str:
    """Consulta si un cheque de una entidad está registrado como denunciado.

    Args:
        codigo_entidad: Código de la entidad bancaria (obtenido de bcra_entidades_cheques)
        numero_cheque: Número del cheque a consultar
    """
    result = await cheques.get_cheque(codigo_entidad, numero_cheque)
    return str(result)


# --- Régimen de Transparencia ---


@mcp.tool()
async def bcra_cajas_ahorro(codigo_entidad: int | None = None) -> str:
    """Lista las cajas de ahorro ofrecidas por las entidades financieras.

    Args:
        codigo_entidad: Código de la entidad financiera para filtrar (opcional)
    """
    result = await transparencia.get_cajas_ahorro(codigo_entidad)
    return str(result)


@mcp.tool()
async def bcra_paquetes_productos(codigo_entidad: int | None = None) -> str:
    """Lista los paquetes de productos ofrecidos por las entidades financieras.

    Args:
        codigo_entidad: Código de la entidad financiera para filtrar (opcional)
    """
    result = await transparencia.get_paquetes_productos(codigo_entidad)
    return str(result)


@mcp.tool()
async def bcra_plazos_fijos(codigo_entidad: int | None = None) -> str:
    """Lista las tasas y condiciones de plazos fijos de las entidades financieras.

    Args:
        codigo_entidad: Código de la entidad financiera para filtrar (opcional)
    """
    result = await transparencia.get_plazos_fijos(codigo_entidad)
    return str(result)


@mcp.tool()
async def bcra_prestamos_prendarios(codigo_entidad: int | None = None) -> str:
    """Lista las tasas y condiciones de préstamos prendarios de las entidades financieras.

    Args:
        codigo_entidad: Código de la entidad financiera para filtrar (opcional)
    """
    result = await transparencia.get_prestamos_prendarios(codigo_entidad)
    return str(result)


@mcp.tool()
async def bcra_prestamos_hipotecarios(codigo_entidad: int | None = None) -> str:
    """Lista las tasas y condiciones de préstamos hipotecarios de las entidades financieras.

    Args:
        codigo_entidad: Código de la entidad financiera para filtrar (opcional)
    """
    result = await transparencia.get_prestamos_hipotecarios(codigo_entidad)
    return str(result)


@mcp.tool()
async def bcra_prestamos_personales(codigo_entidad: int | None = None) -> str:
    """Lista las tasas y condiciones de préstamos personales de las entidades financieras.

    Args:
        codigo_entidad: Código de la entidad financiera para filtrar (opcional)
    """
    result = await transparencia.get_prestamos_personales(codigo_entidad)
    return str(result)


@mcp.tool()
async def bcra_tarjetas_credito(codigo_entidad: int | None = None) -> str:
    """Lista las tasas y condiciones de tarjetas de crédito de las entidades financieras.

    Args:
        codigo_entidad: Código de la entidad financiera para filtrar (opcional)
    """
    result = await transparencia.get_tarjetas_credito(codigo_entidad)
    return str(result)


def main():
    mcp.run()


if __name__ == "__main__":
    main()

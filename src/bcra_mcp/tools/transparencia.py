from bcra_mcp.client import get


async def get_cajas_ahorro(codigo_entidad: int | None = None) -> dict:
    """Lista las cajas de ahorro. Opcionalmente filtra por entidad.

    Args:
        codigo_entidad: Código de la entidad financiera (opcional)
    """
    params = {}
    if codigo_entidad is not None:
        params["codigoEntidad"] = codigo_entidad
    return await get("/transparencia/v1.0/CajasAhorros", params=params)


async def get_paquetes_productos(codigo_entidad: int | None = None) -> dict:
    """Lista los paquetes de productos ofrecidos por las entidades.

    Args:
        codigo_entidad: Código de la entidad financiera (opcional)
    """
    params = {}
    if codigo_entidad is not None:
        params["codigoEntidad"] = codigo_entidad
    return await get("/transparencia/v1.0/PaquetesProductos", params=params)


async def get_plazos_fijos(codigo_entidad: int | None = None) -> dict:
    """Lista las tasas y condiciones de plazos fijos.

    Args:
        codigo_entidad: Código de la entidad financiera (opcional)
    """
    params = {}
    if codigo_entidad is not None:
        params["codigoEntidad"] = codigo_entidad
    return await get("/transparencia/v1.0/PlazosFijos", params=params)


async def get_prestamos_prendarios(codigo_entidad: int | None = None) -> dict:
    """Lista las tasas y condiciones de préstamos prendarios.

    Args:
        codigo_entidad: Código de la entidad financiera (opcional)
    """
    params = {}
    if codigo_entidad is not None:
        params["codigoEntidad"] = codigo_entidad
    return await get("/transparencia/v1.0/PrestamosPrendarios", params=params)


async def get_prestamos_hipotecarios(codigo_entidad: int | None = None) -> dict:
    """Lista las tasas y condiciones de préstamos hipotecarios.

    Args:
        codigo_entidad: Código de la entidad financiera (opcional)
    """
    params = {}
    if codigo_entidad is not None:
        params["codigoEntidad"] = codigo_entidad
    return await get("/transparencia/v1.0/PrestamosHipotecarios", params=params)


async def get_prestamos_personales(codigo_entidad: int | None = None) -> dict:
    """Lista las tasas y condiciones de préstamos personales.

    Args:
        codigo_entidad: Código de la entidad financiera (opcional)
    """
    params = {}
    if codigo_entidad is not None:
        params["codigoEntidad"] = codigo_entidad
    return await get("/transparencia/v1.0/PrestamosPersonales", params=params)


async def get_tarjetas_credito(codigo_entidad: int | None = None) -> dict:
    """Lista las tasas y condiciones de tarjetas de crédito.

    Args:
        codigo_entidad: Código de la entidad financiera (opcional)
    """
    params = {}
    if codigo_entidad is not None:
        params["codigoEntidad"] = codigo_entidad
    return await get("/transparencia/v1.0/TarjetasCredito", params=params)

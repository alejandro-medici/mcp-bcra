import pytest
from unittest.mock import AsyncMock, patch
from bcra_mcp.tools.transparencia import (
    get_cajas_ahorro,
    get_paquetes_productos,
    get_plazos_fijos,
    get_prestamos_personales,
    get_tarjetas_credito,
)

MOCK_RESPONSE = {
    "status": 200,
    "results": [
        {
            "codigoEntidad": 11,
            "descripcionEntidad": "BANCO DE LA NACION ARGENTINA",
            "fechaInformacion": "2024-01-10",
        },
        {
            "codigoEntidad": 72,
            "descripcionEntidad": "BANCO SANTANDER ARGENTINA S.A.",
            "fechaInformacion": "2024-01-10",
        },
    ],
}

MOCK_RESPONSE_FILTRADO = {
    "status": 200,
    "results": [
        {
            "codigoEntidad": 11,
            "descripcionEntidad": "BANCO DE LA NACION ARGENTINA",
            "fechaInformacion": "2024-01-10",
        }
    ],
}


@pytest.mark.asyncio
async def test_get_cajas_ahorro():
    with patch("bcra_mcp.tools.transparencia.get", new=AsyncMock(return_value=MOCK_RESPONSE)):
        result = await get_cajas_ahorro()
        assert result["status"] == 200
        assert len(result["results"]) == 2


@pytest.mark.asyncio
async def test_get_cajas_ahorro_filtrado():
    with patch("bcra_mcp.tools.transparencia.get", new=AsyncMock(return_value=MOCK_RESPONSE_FILTRADO)):
        result = await get_cajas_ahorro(codigo_entidad=11)
        assert result["status"] == 200
        assert result["results"][0]["codigoEntidad"] == 11


@pytest.mark.asyncio
async def test_get_paquetes_productos():
    with patch("bcra_mcp.tools.transparencia.get", new=AsyncMock(return_value=MOCK_RESPONSE)):
        result = await get_paquetes_productos()
        assert result["status"] == 200


@pytest.mark.asyncio
async def test_get_plazos_fijos():
    with patch("bcra_mcp.tools.transparencia.get", new=AsyncMock(return_value=MOCK_RESPONSE)):
        result = await get_plazos_fijos()
        assert result["status"] == 200


@pytest.mark.asyncio
async def test_get_prestamos_personales():
    with patch("bcra_mcp.tools.transparencia.get", new=AsyncMock(return_value=MOCK_RESPONSE)):
        result = await get_prestamos_personales()
        assert result["status"] == 200


@pytest.mark.asyncio
async def test_get_tarjetas_credito():
    with patch("bcra_mcp.tools.transparencia.get", new=AsyncMock(return_value=MOCK_RESPONSE)):
        result = await get_tarjetas_credito()
        assert result["status"] == 200

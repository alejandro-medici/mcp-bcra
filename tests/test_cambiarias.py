import pytest
from unittest.mock import AsyncMock, patch
from bcra_mcp.tools.cambiarias import get_divisas, get_cotizaciones, get_evolucion_moneda

MOCK_DIVISAS = {
    "status": 200,
    "results": [
        {"codigo": "ARS", "denominacion": "PESO"},
        {"codigo": "USD", "denominacion": "DOLAR ESTADOUNIDENSE"},
    ],
}

MOCK_COTIZACIONES = {
    "status": 200,
    "results": {
        "fecha": "2024-01-10",
        "detalle": [
            {
                "codigoMoneda": "USD",
                "descripcion": "DOLAR ESTADOUNIDENSE",
                "tipoPase": 0.001,
                "tipoCotizacion": 808.39,
            },
        ],
    },
}

MOCK_EVOLUCION = {
    "status": 200,
    "metadata": {"resultset": {"count": 1, "offset": 0, "limit": 1000}},
    "results": [
        {
            "fecha": "2024-01-10",
            "detalle": [
                {
                    "codigoMoneda": "USD",
                    "descripcion": "DOLAR ESTADOUNIDENSE",
                    "tipoPase": 0.001,
                    "tipoCotizacion": 808.39,
                }
            ],
        }
    ],
}


@pytest.mark.asyncio
async def test_get_divisas():
    with patch("bcra_mcp.tools.cambiarias.get", new=AsyncMock(return_value=MOCK_DIVISAS)):
        result = await get_divisas()
        assert result["status"] == 200
        assert len(result["results"]) == 2


@pytest.mark.asyncio
async def test_get_cotizaciones_sin_fecha():
    with patch("bcra_mcp.tools.cambiarias.get", new=AsyncMock(return_value=MOCK_COTIZACIONES)):
        result = await get_cotizaciones()
        assert result["status"] == 200
        assert result["results"]["fecha"] == "2024-01-10"


@pytest.mark.asyncio
async def test_get_cotizaciones_con_fecha():
    with patch("bcra_mcp.tools.cambiarias.get", new=AsyncMock(return_value=MOCK_COTIZACIONES)):
        result = await get_cotizaciones(fecha="2024-01-10")
        assert result["status"] == 200


@pytest.mark.asyncio
async def test_get_evolucion_moneda():
    with patch("bcra_mcp.tools.cambiarias.get", new=AsyncMock(return_value=MOCK_EVOLUCION)):
        result = await get_evolucion_moneda("USD", fechadesde="2024-01-01", fechahasta="2024-01-10")
        assert result["status"] == 200
        assert result["results"][0]["detalle"][0]["codigoMoneda"] == "USD"

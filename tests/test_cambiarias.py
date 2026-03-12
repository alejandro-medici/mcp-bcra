import pytest
from unittest.mock import AsyncMock, patch
from bcra_mcp.tools.cambiarias import get_tipos_de_cambio, get_cotizacion

MOCK_TIPOS = {
    "status": 200,
    "results": [
        {"codigo": "BNA", "descripcion": "Banco de la Nación Argentina"},
        {"codigo": "BCO", "descripcion": "Banco Central"},
    ]
}

MOCK_COTIZACION = {
    "status": 200,
    "results": {
        "tipoCambio": "BNA",
        "fecha": "2024-01-10",
        "detalle": [
            {"codigoMoneda": "USD", "descripcion": "Dólar Estadounidense", "tipoPase": "V", "valor": 808.39},
        ]
    }
}


@pytest.mark.asyncio
async def test_get_tipos_de_cambio():
    with patch("bcra_mcp.tools.cambiarias.get", new=AsyncMock(return_value=MOCK_TIPOS)):
        result = await get_tipos_de_cambio()
        assert result["status"] == 200
        assert len(result["results"]) == 2


@pytest.mark.asyncio
async def test_get_cotizacion():
    with patch("bcra_mcp.tools.cambiarias.get", new=AsyncMock(return_value=MOCK_COTIZACION)):
        result = await get_cotizacion("2024-01-10", "BNA")
        assert result["results"]["tipoCambio"] == "BNA"
        assert result["results"]["detalle"][0]["codigoMoneda"] == "USD"

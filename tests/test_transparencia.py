import pytest
from unittest.mock import AsyncMock, patch
from bcra_mcp.tools.transparencia import get_entidades_financieras, get_tasas

MOCK_ENTIDADES = {
    "status": 200,
    "results": [
        {"codigoEntidad": 11, "denominacion": "BANCO DE LA NACION ARGENTINA"},
        {"codigoEntidad": 72, "denominacion": "BANCO SANTANDER ARGENTINA S.A."},
    ]
}

MOCK_TASAS = {
    "status": 200,
    "results": [
        {"codigo": 1, "descripcion": "Tasa Nominal Anual para Préstamos Personales", "valor": 97.0},
        {"codigo": 2, "descripcion": "Tasa Nominal Anual para Caja de Ahorro", "valor": 40.0},
    ]
}


@pytest.mark.asyncio
async def test_get_entidades_financieras():
    with patch("bcra_mcp.tools.transparencia.get", new=AsyncMock(return_value=MOCK_ENTIDADES)):
        result = await get_entidades_financieras()
        assert result["status"] == 200
        assert len(result["results"]) == 2


@pytest.mark.asyncio
async def test_get_tasas():
    with patch("bcra_mcp.tools.transparencia.get", new=AsyncMock(return_value=MOCK_TASAS)):
        result = await get_tasas(11)
        assert result["status"] == 200
        assert len(result["results"]) == 2

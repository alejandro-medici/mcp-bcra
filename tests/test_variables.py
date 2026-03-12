import pytest
from unittest.mock import AsyncMock, patch
from bcra_mcp.tools.variables import get_principales_variables, get_variable_historico

MOCK_VARIABLES = {
    "status": 200,
    "results": [
        {
            "idVariable": 1,
            "cdSerie": 246,
            "descripcion": "Reservas Internacionales del BCRA (en millones de USD)",
            "fecha": "2024-01-10",
            "valor": 23063.0,
        },
        {
            "idVariable": 4,
            "cdSerie": 7927,
            "descripcion": "Tipo de Cambio Minorista ($ por USD) Promedio vendedor",
            "fecha": "2024-01-10",
            "valor": 808.39,
        },
    ],
}

MOCK_HISTORICO = {
    "status": 200,
    "results": [
        {"idVariable": 1, "fecha": "2024-01-02", "valor": 23100.0},
        {"idVariable": 1, "fecha": "2024-01-03", "valor": 23050.0},
    ],
}


@pytest.mark.asyncio
async def test_get_principales_variables():
    with patch("bcra_mcp.tools.variables.get", new=AsyncMock(return_value=MOCK_VARIABLES)):
        result = await get_principales_variables()
        assert result["status"] == 200
        assert len(result["results"]) == 2
        assert result["results"][0]["idVariable"] == 1


@pytest.mark.asyncio
async def test_get_variable_historico():
    with patch("bcra_mcp.tools.variables.get", new=AsyncMock(return_value=MOCK_HISTORICO)):
        result = await get_variable_historico(1, "2024-01-02", "2024-01-03")
        assert result["status"] == 200
        assert len(result["results"]) == 2

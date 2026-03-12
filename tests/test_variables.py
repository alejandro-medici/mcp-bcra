import pytest
from unittest.mock import AsyncMock, patch
from bcra_mcp.tools.variables import get_variables, get_variable_historico

MOCK_VARIABLES = {
    "status": 200,
    "metadata": {"resultset": {"count": 2, "offset": 0, "limit": 1000}},
    "results": [
        {
            "idVariable": 1,
            "descripcion": "Reservas internacionales",
            "categoria": "Principales Variables",
            "periodicidad": "D",
            "unidadExpresion": "En millones de USD",
            "ultFechaInformada": "2024-01-10",
            "ultValorInformado": 23063.0,
        },
        {
            "idVariable": 4,
            "descripcion": "Tipo de Cambio Minorista",
            "categoria": "Principales Variables",
            "periodicidad": "D",
            "unidadExpresion": "Pesos",
            "ultFechaInformada": "2024-01-10",
            "ultValorInformado": 808.39,
        },
    ],
}

MOCK_HISTORICO = {
    "status": 200,
    "metadata": {"resultset": {"count": 2, "offset": 0, "limit": 1000}},
    "results": [
        {
            "idVariable": 1,
            "detalle": [
                {"fecha": "2024-01-02", "valor": 23100.0},
                {"fecha": "2024-01-03", "valor": 23050.0},
            ],
        }
    ],
}


@pytest.mark.asyncio
async def test_get_variables():
    with patch("bcra_mcp.tools.variables.get", new=AsyncMock(return_value=MOCK_VARIABLES)):
        result = await get_variables()
        assert result["status"] == 200
        assert len(result["results"]) == 2
        assert result["results"][0]["idVariable"] == 1


@pytest.mark.asyncio
async def test_get_variables_con_filtros():
    with patch("bcra_mcp.tools.variables.get", new=AsyncMock(return_value=MOCK_VARIABLES)):
        result = await get_variables(categoria="Principales Variables", periodicidad="D")
        assert result["status"] == 200


@pytest.mark.asyncio
async def test_get_variable_historico():
    with patch("bcra_mcp.tools.variables.get", new=AsyncMock(return_value=MOCK_HISTORICO)):
        result = await get_variable_historico(1, desde="2024-01-02", hasta="2024-01-03")
        assert result["status"] == 200
        assert result["results"][0]["idVariable"] == 1

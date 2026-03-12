import pytest
from unittest.mock import AsyncMock, patch
from bcra_mcp.tools.deudores import get_deudores, get_deudores_historico, get_cheques_rechazados

MOCK_DEUDORES = {
    "status": 200,
    "results": {
        "identificacion": 20123456789,
        "denominacion": "GARCIA JUAN CARLOS",
        "periodos": [
            {
                "periodo": "202407",
                "entidades": [
                    {"entidad": "BANCO DE LA NACION ARGENTINA", "situacion": 1, "monto": 59.0}
                ],
            }
        ],
    },
}

MOCK_HISTORICO = {
    "status": 200,
    "results": {
        "identificacion": 20123456789,
        "denominacion": "GARCIA JUAN CARLOS",
        "periodos": [],
    },
}

MOCK_CHEQUES = {
    "status": 200,
    "results": {
        "identificacion": 20123456789,
        "denominacion": "GARCIA JUAN CARLOS",
        "causales": [],
    },
}


@pytest.mark.asyncio
async def test_get_deudores():
    with patch("bcra_mcp.tools.deudores.get", new=AsyncMock(return_value=MOCK_DEUDORES)):
        result = await get_deudores("20123456789")
        assert result["status"] == 200
        assert result["results"]["denominacion"] == "GARCIA JUAN CARLOS"


@pytest.mark.asyncio
async def test_get_deudores_historico():
    with patch("bcra_mcp.tools.deudores.get", new=AsyncMock(return_value=MOCK_HISTORICO)):
        result = await get_deudores_historico("20123456789")
        assert result["status"] == 200
        assert result["results"]["identificacion"] == 20123456789


@pytest.mark.asyncio
async def test_get_cheques_rechazados():
    with patch("bcra_mcp.tools.deudores.get", new=AsyncMock(return_value=MOCK_CHEQUES)):
        result = await get_cheques_rechazados("20123456789")
        assert result["status"] == 200

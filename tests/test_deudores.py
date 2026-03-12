import pytest
from unittest.mock import AsyncMock, patch
from bcra_mcp.tools.deudores import get_deudores, get_deudores_historico

MOCK_DEUDORES = {
    "status": 200,
    "results": {
        "identificacion": 20123456789,
        "denominacion": "GARCIA JUAN CARLOS",
        "periodos": [
            {
                "periodo": "2024-01",
                "entidades": [
                    {"entidad": 11, "situacion": 1, "monto": 150000}
                ]
            }
        ]
    }
}

MOCK_HISTORICO = {
    "status": 200,
    "results": {
        "identificacion": 20123456789,
        "periodos": []
    }
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

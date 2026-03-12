import pytest
from unittest.mock import AsyncMock, patch
from bcra_mcp.tools.cheques import get_entidades, get_cheques_rechazados, get_cheque_por_numero

MOCK_ENTIDADES = {
    "status": 200,
    "results": [
        {"codigoEntidad": 11, "denominacion": "BANCO DE LA NACION ARGENTINA"},
        {"codigoEntidad": 72, "denominacion": "BANCO SANTANDER ARGENTINA S.A."},
    ]
}

MOCK_CHEQUES = {
    "status": 200,
    "results": {
        "numeroCuenta": "0",
        "causal": "0",
        "cheques": []
    }
}

MOCK_CHEQUE = {
    "status": 200,
    "results": {
        "numeroCheque": 12345678,
        "codigoEntidad": 11,
        "denominacion": "BANCO DE LA NACION ARGENTINA",
        "causal": "2"
    }
}


@pytest.mark.asyncio
async def test_get_entidades():
    with patch("bcra_mcp.tools.cheques.get", new=AsyncMock(return_value=MOCK_ENTIDADES)):
        result = await get_entidades()
        assert result["status"] == 200
        assert len(result["results"]) == 2


@pytest.mark.asyncio
async def test_get_cheques_rechazados():
    with patch("bcra_mcp.tools.cheques.get", new=AsyncMock(return_value=MOCK_CHEQUES)):
        result = await get_cheques_rechazados("20123456789")
        assert result["status"] == 200


@pytest.mark.asyncio
async def test_get_cheque_por_numero():
    with patch("bcra_mcp.tools.cheques.get", new=AsyncMock(return_value=MOCK_CHEQUE)):
        result = await get_cheque_por_numero(11, 12345678)
        assert result["results"]["numeroCheque"] == 12345678

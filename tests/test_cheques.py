import pytest
from unittest.mock import AsyncMock, patch
from bcra_mcp.tools.cheques import get_entidades, get_cheque

MOCK_ENTIDADES = {
    "status": 200,
    "results": [
        {"codigoEntidad": 11, "denominacion": "BANCO DE LA NACION ARGENTINA"},
        {"codigoEntidad": 72, "denominacion": "BANCO SANTANDER ARGENTINA S.A."},
    ],
}

MOCK_CHEQUE_DENUNCIADO = {
    "status": 200,
    "results": {
        "numeroCheque": 20377516,
        "denunciado": True,
        "fechaProcesamiento": "2024-05-24",
        "denominacionEntidad": "BANCO DE LA NACION ARGENTINA",
        "detalles": [
            {"sucursal": 524, "numeroCuenta": 5240055962, "causal": "Denunciado por tercero"}
        ],
    },
}

MOCK_CHEQUE_NO_DENUNCIADO = {
    "status": 200,
    "results": {
        "numeroCheque": 203775991,
        "denunciado": False,
        "fechaProcesamiento": "2024-05-24",
        "denominacionEntidad": "BANCO DE LA NACION ARGENTINA",
        "detalles": [],
    },
}


@pytest.mark.asyncio
async def test_get_entidades():
    with patch("bcra_mcp.tools.cheques.get", new=AsyncMock(return_value=MOCK_ENTIDADES)):
        result = await get_entidades()
        assert result["status"] == 200
        assert len(result["results"]) == 2


@pytest.mark.asyncio
async def test_get_cheque_denunciado():
    with patch("bcra_mcp.tools.cheques.get", new=AsyncMock(return_value=MOCK_CHEQUE_DENUNCIADO)):
        result = await get_cheque(11, 20377516)
        assert result["status"] == 200
        assert result["results"]["denunciado"] is True


@pytest.mark.asyncio
async def test_get_cheque_no_denunciado():
    with patch("bcra_mcp.tools.cheques.get", new=AsyncMock(return_value=MOCK_CHEQUE_NO_DENUNCIADO)):
        result = await get_cheque(11, 203775991)
        assert result["results"]["denunciado"] is False

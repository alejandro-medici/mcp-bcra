import httpx

BASE_URL = "https://api.bcra.gob.ar"

_client: httpx.AsyncClient | None = None


def get_client() -> httpx.AsyncClient:
    global _client
    if _client is None:
        _client = httpx.AsyncClient(
            base_url=BASE_URL,
            timeout=30.0,
            verify=True,
        )
    return _client


async def get(path: str, params: dict | None = None) -> dict:
    client = get_client()
    response = await client.get(path, params=params)
    response.raise_for_status()
    return response.json()

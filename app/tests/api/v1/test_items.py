from fastapi.testclient import TestClient


def test_get_itmes(
        client: TestClient
):
    response = client.get("/v1/items")
    assert response.status_code == 200

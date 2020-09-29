
from requests import Response


def test_get_all_circuits(test_client):
    response: Response = test_client.get('/api/v1/circuits')
    assert response.status_code == 200
    assert response.json() is not None

    test_circuits = response.json()

    assert len(test_circuits) == 3

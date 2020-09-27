import pytest

from requests import Response


@pytest.mark.skip('not implemented yet')
def test_get_all_circuits(mongodb, test_client):
    response: Response = test_client.get('/api/v1/circuits')
    assert response.status_code == 200
    assert response.json() is not None

    test_circuits = response.json()

    print(test_circuits)
    assert len(test_circuits) == 5

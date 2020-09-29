from requests import Response


def test_get_all_circuits(test_client):
    response: Response = test_client.get('/api/v1/circuits')
    assert response.status_code == 200
    assert response.json() is not None

    test_circuits = response.json()

    assert len(test_circuits) == 3


def test_add_circuit_with_good_data_returns_204(test_client):
    circuit = {
        "cid": "yelled-at-dirt",
        "provider": "Lumina",
        "customers": []
    }

    response: Response = test_client.post('/api/v1/circuits', data=circuit)

    assert response.status_code == 204
    assert response.json() is not None

    test = response.json()

    assert test == "{}"

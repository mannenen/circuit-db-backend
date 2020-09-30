from requests import Response


def test_get_all_circuits(test_client):
    response: Response = test_client.get('/api/v1/circuits')
    assert response.status_code == 200
    assert response.json() is not None

    test_circuits = response.json()

    assert len(test_circuits) == 3


def test_add_circuit_with_good_data_returns_201(test_client):
    circuit = {
        "cid": "yelled-at-dirt",
        "provider": "Lumina",
        "customers": []
    }

    response: Response = test_client.post('/api/v1/circuits', json=circuit)

    assert response.status_code == 201
    assert response.json() == circuit


def test_add_circuit_without_cid_returns_bad_request(test_client):
    circuit = {
        "provider": "Jummbbile",
        "customers": []
    }

    response: Response = test_client.post('/api/v1/circuits', json=circuit)

    assert response.status_code == 400
    assert response.json()["detail"] == "Missing circuit ID"


def test_add_circuit_only_requires_cid_and_provider(test_client):
    circuit = {
        "provider": "Kielelcccdmem",
        "cid": ":300Lr339e9/340rd9foikVNegjskfd"
    }

    response: Response = test_client.post('/api/v1/circuits', json=circuit)

    assert response.status_code == 201
    assert response.json() == {
        "provider": "Kielelcccdmem",
        "cid": ":300Lr339e9/340rd9foikVNegjskfd",
        "customers": []
    }


def test_delete_circuits_returns_method_not_allowed(test_client):
    response: Response = test_client.delete('/api/v1/circuits')

    assert response.status_code == 405

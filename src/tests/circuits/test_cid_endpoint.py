from requests import Response


def test_get_circuit_by_valid_cid_returns_200_and_circuit(test_client):
    test: Response = test_client.get('/api/v1/circuits/farted-chair')

    assert test.status_code == 200
    assert test.json()['customers'] == []
    assert test.json()['cid'] == "farted-chair"
    assert test.json()['provider'] == "EAST TEL"

def test_get_circuit_by_invalid_cid_returns_404_and_detail_message(test_client):
    test: Response = test_client.get('/api/v1/circuits/haberdasher-surprise')

    assert test.status_code == 404
    assert test.json()['detail'] == "could not find circuit with CID haberdasher-surprise"

def test_delete_circuit_by_valid_cid_returns_204(test_client):
    test: Response = test_client.delete('/api/v1/circuits/farted-chair')

    assert test.status_code == 204

def test_delete_circuit_by_invalid_cid_returns_404_and_detail(test_client):
    test: Response = test_client.delete('/api/v1/circuits/haberdasher-surprise')

    assert test.status_code == 404
    assert test.json()['detail'] == "could not find circuit with CID haberdasher-surprise"

def test_patch_by_invalid_cid_returns_404_and_detail(test_client):
    updates = {
        "provider": "Produnce Meangue",
        "a": {
            "street_1": "1233231231 Fedkfj Ave",
            "city": "Alexandria",
            "state": "LA",
            "zip_code": "70749"
        }
    }

    test: Response = test_client.patch('/api/v1/circuits/farted-chair', json=updates)

    assert test.status_code == 200
    
    j = test.json()
    assert j['provider'] == "Produnce Meangue"
    assert j['cid'] == "farted-chair"

def test_update_cid_fails_with_403_and_detail(test_client):
    updates = {
        "cid": "haberdasher-surprise"
    }

    test: Response = test_client.patch('/api/v1/circuits/farted-chair', json=updates)

    assert test.status_code == 403
    assert test.json()['detail'] == "Forbidden to change CID of existing circuit, create a new circuit instead"
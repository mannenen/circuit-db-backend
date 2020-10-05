from requests import Response


def test_provider_collection_returns_200_and_list_of_provider_names(test_client):
    test: Response = test_client.get('/api/v1/providers')

    assert test.status_code == 200
    assert "QuanturyLink" in test.json()['providers']
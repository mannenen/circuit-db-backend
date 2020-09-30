from backend.database.mongo import MongoDatabase


def test_get_all_circuits_returns_array(db: MongoDatabase):
    test = db.get_all_circuits()

    assert isinstance(test, list)


def test_get_all_circuits_returns_three_records(db: MongoDatabase):
    test = db.get_all_circuits()

    assert len(test) == 3


def test_get_circuit_by_invalid_cid_returns_None(db: MongoDatabase):
    test = db.get_circuit_by_cid("jumping-jeremiah")

    assert test is None


def test_get_circuit_by_valid_cid_returns_circuit(db: MongoDatabase):
    test = db.get_circuit_by_cid("excellent-eggplant")

    assert "provider" in test.keys()


def test_add_circuit_returns_created_circuit(db: MongoDatabase):
    circuit = {
        "provider": 'sfdkjsakjasdfkj',
        "cid": 'safkjewkjsd',
        "customers": []
    }
    test = db.add_circuit(circuit)

    assert test == circuit


def test_add_circuit_without_customers_adds_empty_customer_array(db: MongoDatabase):
    circuit = {
        "provider": "FFJDKFJKDFJFDJ",
        "cid": "weifsudikfj30dfksdjfsdfkj"
    }
    test = db.add_circuit(circuit)

    assert "customers" in test.keys()
    assert test["customers"] == []

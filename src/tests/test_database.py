import pytest

from backend.database.mongo import MongoDatabase


def test_get_document_count_returns_correct_count(db: MongoDatabase):
    test = db.count()

    assert test == 3


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
    result, test = db.add_circuit(circuit)

    assert result == True
    assert test == circuit


def test_add_circuit_without_customers_adds_empty_customer_array(db: MongoDatabase):
    circuit = {
        "provider": "FFJDKFJKDFJFDJ",
        "cid": "weifsudikfj30dfksdjfsdfkj"
    }
    result, test = db.add_circuit(circuit)

    assert result == True
    assert "customers" in test.keys()
    assert test["customers"] == []


def test_delete_circuit_by_cid_only_deletes_one_item_from_db(db: MongoDatabase):
    cid = "farted-chair"
    
    count_before = db.count()
    result = db.delete_circuit_by_cid(cid)
    count_after = db.count()

    assert result is True
    assert count_before == count_after + 1


def test_update_circuit_by_cid_returns_updated_circuit(db: MongoDatabase):
    cid = "farted-chair"
    updates = {
        "provider": "Produnce Meangue",
        "a": {
            "street_1": "1233231231 Fedkfj Ave",
            "city": "Alexandria",
            "state": "LA",
            "zip_code": "70749"
        }
    }

    test = db.update_circuit_by_cid(cid, updates)

    assert test is not None


def test_update_circuit_by_cid_returns_none_if_attempt_to_modify_cid(db: MongoDatabase):
    cid = "farted-chair"
    updates = {
        "cid": "haberdasher-surprise"
    }

    updated =  db.update_circuit_by_cid(cid, updates)
    assert updated is None

    modified = db.get_circuit_by_cid("haberdasher-surprise")
    assert modified is None

from pymongo import ReturnDocument
from pymongo.database import Database
from pymongo.collection import Collection


class MongoDatabase:
    def __init__(self, db: Database):
        self.circuits: Collection = db.circuits
        self.fields = {
            "_id": False,
            "cid": True,
            "provider": True,
            "customers": True,
            "a": True,
            "z": True
        }

    def count(self):
        return self.circuits.count_documents({})

    def get_all_circuits(self):
        return [circuit for circuit in self.circuits.find(projection=self.fields)]

    def get_circuit_by_cid(self, cid):
        return self.circuits.find_one(filter={"cid": cid}, projection=self.fields)

    def add_circuit(self, circuit: dict):
        if "customers" not in circuit.keys():
            circuit["customers"] = []
        to_insert = circuit.copy()

        if self.circuits.count_documents({"cid": to_insert["cid"]}) > 0:
            print("Found documents with duplicate cid")
            return False, {"detail": "Duplicate CID", "status_code": 409}

        insert = self.circuits.insert_one(to_insert)
        if insert is None:
            return False, {"detail": "unknown error", "status_code": 400}

        return True, self.circuits.find_one({"_id": insert.inserted_id}, {"_id": False})

    def delete_circuit_by_cid(self, cid: str):
        result = self.circuits.delete_one({ "cid": cid })

        return result.deleted_count == 1
    
    def update_circuit_by_cid(self, cid: str, updates: dict):
        if "cid" in updates.keys():
            return None

        return self.circuits.find_one_and_update({"cid": cid},
                                                 {"$set": updates},
                                                 projection=self.fields,
                                                 return_document=ReturnDocument.AFTER)

    def get_all_providers(self):
        return self.circuits.distinct("provider")

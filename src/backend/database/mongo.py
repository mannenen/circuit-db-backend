from pymongo.database import Database


class MongoDatabase:
    def __init__(self, db: Database):
        self.db = db
        self.fields = {
            "_id": False,
            "cid": True,
            "provider": True,
            "customers": True,
            "a": True,
            "z": True
        }

    def get_all_circuits(self):
        return [circuit for circuit in self.db.circuits.find(projection=self.fields)]

    def get_circuit_by_cid(self, cid):
        return self.db.circuits.find_one(filter={"cid": cid})

    def add_circuit(self, circuit: dict):
        if "customers" not in circuit.keys():
            circuit["customers"] = []
        to_insert = circuit.copy()

        if self.db.circuits.count_documents({"cid": to_insert["cid"]}) > 0:
            print("Found documents with duplicate cid")
            return False, {"detail": "Duplicate CID", "status_code": 409}

        insert = self.db.circuits.insert_one(to_insert)
        if insert is None:
            return False, {"detail": "unknown error", "status_code": 400}

        return True, self.db.circuits.find_one({"_id": insert.inserted_id}, {"_id": False})

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

    def add_circuit(self, circuit: dict = {}):
        pass

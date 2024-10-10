from repository.base_repository import BaseRepository


class AccidentRepository(BaseRepository):
    def __init__(self, collection):
        super().__init__(collection)

    def find_by_query(self, query):
        res = (self.collection.find(query, {"_id": 1}))
        return list(res)

    def grop_by_query(self, query):
        res = self.collection.aggregate(query)
        return list(res)
from repository.base_repository import BaseRepository


class BeatsRepository(BaseRepository):
    def __init__(self, collection):
        super().__init__(collection)

    def add_accident(self, beat, accident_id):
        result = self.collection.update_one(
            {"beat": beat},
            {"$push": {"accidents": accident_id}},
            upsert = True
        )
        return result.modified_count

    def get_by_beat(self, beat):
        res = self.collection.find_one({"beat": beat})
        return res['accidents']


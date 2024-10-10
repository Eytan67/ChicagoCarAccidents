from bson import ObjectId

class BaseRepository:
    def __init__(self, collection):
        self.collection = collection

    def drop_collection(self):
        self.collection.drop()

    def add(self, item):
        return self.collection.insert_one(item).inserted_id

    def add_many(self, items):
        return self.collection.insert_many(items)

    def get_all(self):
        return self.collection.find()

    def get_by_id(self, item_id):
        return self.collection.find_one({"_id": ObjectId(item_id)})

    def update(self, item_id, updated_data):
        return self.collection.update_one({"_id": ObjectId(item_id)}, {"$set": updated_data})

    def delete(self, item_id):
        return self.collection.delete_one({"_id": ObjectId(item_id)})
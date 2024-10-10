from flask import Flask
from pymongo import MongoClient

class Database:
    def __init__(self, app: Flask):
        self.client = MongoClient(app.config['MONGO_URI'])
        self.db = self.client.database01

    def get_collection(self, name):
        return self.db[name]

    def close_connection(self):
        if self.client:
            self.client.close()
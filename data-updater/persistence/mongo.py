from config.config import config
from persistence.db import Db


class Mongo(Db):
    __DB_NAME = 'stay_safe'

    def __init__(self, env: config, collection_name: str):
        self._env = env
        self._collection_name = collection_name

    def __enter__(self):
        from pymongo import MongoClient
        self.__client = MongoClient(self._env.get_database_conn_string())

        db = self.__client.get_database(self.__DB_NAME)
        self._collection = db.get_collection(self._collection_name)

        return self

    def __exit__(self, type, value, traceback):
        self.__client.close()

    def insert_one(self, document) -> any:
        return self.__collection.insert_one(document).inserted_id

    def insert_many(self, documents: []) -> any:
        return self.__collection.insert_many(documents).inserted_ids

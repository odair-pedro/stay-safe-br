from config.config import config
from models.city import City
from persistence.mongo import Mongo


class CityPersistence(Mongo):
    __COLLECTION_NAME = 'city'

    def __init__(self, env: config):
        super().__init__(env, self.__COLLECTION_NAME)

    def insert_one(self, city):
        document = self.__parse_city(city)
        super().insert_one(document)

    def insert_many(self, cities: []) -> any:
        docs = [len(cities)]
        for city in cities:
            docs.append(self.__parse_city(city))
        return super().insert_many(docs)

    @staticmethod
    def __parse_city(city: City):
        return {
            "_id": city.ibge_code,
            "ibge_code": city.ibge_code,
            "name": city.name,
            "state": city.state,
            "estimated_population": city.estimated_population
        }

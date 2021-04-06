from config.config import config
from models.historic import Historic
from persistence.mongo import Mongo


class HistoricPersistence(Mongo):
    __COLLECTION_NAME = 'historic'

    def __init__(self, env: config):
        super().__init__(env, self.__COLLECTION_NAME)

    def insert_one(self, document):
        parsed_doc = self.__parse_history(document)
        super().insert_one(parsed_doc)

    def insert_many(self, documents: []) -> any:
        parsed_docs = []
        for doc in documents:
            parsed_docs.append(self.__parse_history(doc))
        return super().insert_many(parsed_docs)

    @staticmethod
    def __parse_historic(hist: Historic):
        return {
            "_id": hist.ibge_code,
            "ibge_code": hist.ibge_code,
            "name": hist.name,
            "state": hist.state,
            "estimated_population": hist.estimated_population,
            "epidemiological_week": hist.epidemiological_week,
            "date": hist.date,
            "order": hist.order
        }

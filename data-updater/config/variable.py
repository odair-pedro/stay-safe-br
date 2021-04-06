import os

from config.config import config


class Env(config):
    __ENV_DB_CONN_STRING = 'STAY_SAFE_DB_CONN_STRING'

    def get_database_conn_string(self) -> str:
        return os.getenv(self.__ENV_DB_CONN_STRING)

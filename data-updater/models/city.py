from datetime import date


class City:
    _DELIMITER = ','
    _IDX_IBGE_CODE = 1
    _IDX_NAME = 0
    _IDX_STATE = 15
    _IDX_ESTIMATED_POPULATION = 4
    _IDX_LAST_DATE_UPDATED = 10
    _IDX_LAST_ORDER_UPDATED = 12
    _IDX_LAST_CONFIRMED_CASES = 8
    _IDX_LAST_CONFIRMED_CASES_PERCENT = 9
    _IDX_LAST_DEATH_RATE = 11
    _IDX_NEW_CONFIRMED = 16
    _IDX_NEW_DEATH = 17

    _ibge_code: int = None
    _name: str = None
    _state: str = None
    _estimated_population: int = None
    _last_date_updated: date = None
    _last_order_updated: int = None
    _last_confirmed_cases: int = None
    _last_confirmed_cases_percent: float = None
    _last_death_rate: float = None
    _new_confirmed: int = None
    _new_death: int = None

    def __init__(self, data: str):
        self._source = data.split(self._DELIMITER)
        if not self.__check_source_isvalid():
            return

        self._ibge_code = int(self._source[self._IDX_IBGE_CODE])
        self._name = self._source[self._IDX_NAME]

    @property
    def ibge_code(self) -> int:
        return self._ibge_code

    @property
    def name(self) -> str:
        return self._name

    @property
    def state(self) -> str:
        return self._state

    @property
    def estimated_population(self) -> int:
        return self._estimated_population

    def is_valid(self) -> bool:
        return bool(self.ibge_code and self.name)

    def map_values(self) -> bool:
        try:
            self._state = self._source[self._IDX_STATE]
            self._estimated_population = int(self._source[self._IDX_ESTIMATED_POPULATION])
            self._last_date_updated = date.fromisoformat(self._source[self._IDX_LAST_DATE_UPDATED])
            self._last_order_updated = int(self._source[self._IDX_LAST_ORDER_UPDATED])
        except Exception as err:
            print(err)
            return False

        return True

    def __check_source_isvalid(self) -> bool:
        ic = self._source[self._IDX_IBGE_CODE]
        return ic.isdigit()

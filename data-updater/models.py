class City:
    _delimiter = ','
    _idx_name = 0
    _idx_state = 15
    _idx_ibge_code = 1
    _idx_estimated_population = 4
    _idx_last_date_updated = 10
    _idx_last_order_updated = 12
    _idx_last_confirmed_cases = 8
    _idx_last_confirmed_cases_percent = 9
    _idx_last_death_rate = 11
    _idx_new_confirmed = 16
    _idx_new_death = 17

    def __init__(self, data: str):
        self._map(data)

    def _map(self, data: str):
        values = data.split(self._delimiter)
        self._name = values[self._idx_name]
        self._state = values[self._idx_state]

    @property
    def name(self) -> str:
        return self._name

    @property
    def state(self) -> str:
        return self._state


class History:
    _delimiter = ','
    _idx_epidemiological_week = 3
    _idx_date = 10
    _idx_order = 12

    def __init__(self, data: str):
        self._city = City(data)
        self._map(data)

    def _map(self, data: str):
        values = data.split(self._delimiter)
        self.epidemiological_week = values[self._idx_epidemiological_week]

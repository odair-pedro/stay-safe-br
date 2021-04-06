from datetime import date

from models.city import City


class Historic(City):
    _IDX_EPIDEMIOLOGICAL_WEEK = 3
    _IDX_DATE = 10
    _IDX_ORDER = 12
    _IDX_IS_REPEATED = 7

    _epidemiological_week: int
    _date: date
    _order: int

    def __init__(self, data: str):
        super().__init__(data)

    @property
    def epidemiological_week(self) -> int:
        return self._epidemiological_week

    @property
    def date(self) -> date:
        return self._date

    @property
    def order(self) -> int:
        return self._order

    def map_values(self) -> bool:
        try:
            super().map_values()
            self._epidemiological_week = self._source[self._IDX_EPIDEMIOLOGICAL_WEEK]
            self._date = self._source[self._IDX_DATE]
            self._order = self._source[self._IDX_ORDER]
        except Exception as err:
            print(err)
            return False

        return True

    def is_valid(self) -> bool:
        return City.is_valid(self) and self._source[self._IDX_IS_REPEATED] != '1'

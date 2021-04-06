import datasource
from config.variable import Env
from models.historic import Historic
from persistence.mongo_historic import HistoricPersistence


def update_data():
    historic = []
    with datasource.load() as ds:
        while not ds.eof():
            hist = Historic(ds.read())
            if not hist.is_valid():
                continue
            if not hist.map_values():
                continue

            historic.append(hist)
            print('appending...')

    with HistoricPersistence(Env()) as hist_persistence:
        hist_persistence.insert_many(historic)

    print('update has been finalized')


if __name__ == '__main__':
    update_data()

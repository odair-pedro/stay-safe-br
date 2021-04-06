import datasource
from config.variable import Env
from models.historic import Historic
from persistence.mongo_historic import HistoricPersistence


def update_data():
    with HistoricPersistence(Env()) as hist_persistence:
        with datasource.load() as ds:
            while not ds.eof():
                hist = Historic(ds.read())
                if not hist.is_valid():
                    continue
                if not hist.map_values():
                    continue

                hist_persistence.insert_one(hist)
                print('inserting...')

    print('update has been finalized')


if __name__ == '__main__':
    update_data()

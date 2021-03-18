import datasource


def update_data():
    with datasource.load() as ds:
        while not ds.eof():
            print(ds.read())


if __name__ == '__main__':
    update_data()

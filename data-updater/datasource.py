import gzip
import os
import shutil

import requests


class DataSource:

    def __init__(self, file_path: str, size: int):
        self._size = size
        self._file_path = file_path
        self._cursor = 0

    def __enter__(self):
        self._file = open(self._file_path, 'rt')
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def close(self) -> None:
        self._file.close()
        os.remove(self._file.name)

    def eof(self) -> bool:
        return self._cursor == self._size - 1

    def read(self) -> str:
        txt = self._file.readline()
        if txt != '':
            self._cursor += 1
        return txt


def load() -> DataSource:
    url = 'https://data.brasil.io/dataset/covid19/caso_full.csv.gz'
    print('Downloading data source...')

    r = requests.get(url)
    print('Data source has been downloaded. Status Code: ', r.status_code)

    tmp_path = './.ds-temp'
    tmp_path_gz = tmp_path + '.gz'
    with open(tmp_path_gz, 'wb') as f:
        f.write(r.content)
        f.flush()

    try:
        print('Unzipping data source file...')
        with gzip.open(tmp_path_gz, 'rb') as f_in:
            with open(tmp_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
    finally:
        os.remove(tmp_path_gz)

    size = 0
    print('Calculating file...')
    with open(tmp_path, 'rt') as f_txt:
        for _ in f_txt:
            size += 1
    print('Data source size ', size)

    return DataSource(tmp_path, size)

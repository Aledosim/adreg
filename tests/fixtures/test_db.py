from peewee import SqliteDatabase
from src.data import Data
import pytest
import os

@pytest.fixture()
def test_db(tmpdir):
    test_db = tmpdir.join('test.db')
    os.environ['ADREG_TEST_DB'] = str(test_db)
    yield
    del os.environ['ADREG_TEST_DB']

@pytest.fixture()
def models(test_db):
    database = SqliteDatabase(os.environ['ADREG_TEST_DB'])

    with database.bind_ctx(Data.models):
        yield dict([(model.__name__, model) for model in Data.models])


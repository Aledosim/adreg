from peewee import SqliteDatabase
import pytest
import os

@pytest.fixture(autouse=True)
def test_db(tmpdir):
    test_db = tmpdir.join('test.db')
    os.environ['ADREG_TEST_DB'] = str(test_db)
    yield
    del os.environ['ADREG_TEST_DB']

@pytest.fixture()
def get_models():
    def inner(models_list):
        database = SqliteDatabase(os.environ['ADREG_TEST_DB'])
        database.bind(models_list)
        return dict([(model.__name__, model) for model in models_list])

    return inner


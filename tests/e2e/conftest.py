from peewee import SqliteDatabase
import pytest
import os
import shutil
from pathlib import Path

@pytest.fixture()
def get_models():
    def inner(models_list):
        database = SqliteDatabase(os.environ['ADREG_TEST_DB'])
        database.bind(models_list)
        return dict([(model.__name__, model) for model in models_list])

    return inner

@pytest.fixture()
def apply_test_db():
    src_db = Path('tests').joinpath('test.db')
    dst_db = os.environ['ADREG_TEST_DB']
    shutil.copyfile(src_db, dst_db)

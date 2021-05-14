import pytest
from peewee import Model
import os
import src

from src.models.base import BaseModel, get_database

class TestBaseModel:

    def test_base_attributes(self, mocker):
        mocker.patch('src.models.base.DateTimeField')
        mocker.patch('src.models.base.AutoField')

        assert issubclass(BaseModel, Model)
        assert BaseModel.created_at == src.models.base.DateTimeField()
        assert BaseModel.updated_at == src.models.base.DateTimeField()
        assert BaseModel.id == src.models.base.AutoField()

    def test_get_database_without_test_env(self, mocker):
        mock_db = mocker.patch('src.models.base.SqliteDatabase')
        del os.environ['ADREG_TEST_DB']

        get_database()

        mock_db.assert_called_once_with('adreg.db')

    def test_get_database_with_test_env(self, mocker):
        mock_db = mocker.patch('src.models.base.SqliteDatabase')
        os.environ['ADREG_TEST_DB'] = 'test.db'

        get_database()

        mock_db.assert_called_once_with('test.db')

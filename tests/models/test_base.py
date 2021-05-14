import pytest
from peewee import Model
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

    def test_get_database(self, mocker):
        mock_db = mocker.patch('src.models.base.SqliteDatabase')

        get_database()

        mock_db.assert_called_once_with(None)

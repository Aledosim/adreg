from peewee import Model
import src

from src.models.base import BaseModel


class TestBaseModel:

    def test_base_attributes(self, mocker):
        mocker.patch('src.models.base.DateTimeField')
        mocker.patch('src.models.base.AutoField')

        assert issubclass(BaseModel, Model)
        assert BaseModel.created_at == src.models.base.DateTimeField()
        assert BaseModel.updated_at == src.models.base.DateTimeField()
        assert BaseModel.id == src.models.base.AutoField()

import pytest
from peewee import SqliteDatabase

import src

from src.data import Data


class TestData:

    def test_class_att_database(self):
        assert isinstance(src.data.Data.database, SqliteDatabase)

    def test_init(self, mocker):
        mocker.patch('src.data.Data.database')
        mock_create_tables = mocker.patch('src.data.Data.create_tables')

        Data()

        mock_create_tables.assert_called_once()

    def test_create_tables(self, mocker, monkeypatch):
        monkeypatch.setattr(Data, 'create_tables', Data.create_tables.__wrapped__)
        mock_db = mocker.patch('src.data.Data.database')

        data = Data()

        mock_db.create_tables.assert_called_once_with(data.models)

    def test_get_or_create_ad(self, mocker, ad_input_dto):
        mocker.patch('src.data.Data.database')
        mocker.patch('src.data.Data.create_tables')
        ad_entry_class =  mocker.patch('src.data.AdEntryDTO')

        ad_class = mocker.patch('src.data.Ad')
        ad = mocker.Mock()
        ad_class.get_or_create.return_value = ad, mocker.Mock()

        data = Data()
        result = data.get_or_create_ad.__wrapped__(data, ad_input_dto)

        ad_class.get_or_create.assert_called_once_with(
            name=ad_input_dto.name,
            client=ad_input_dto.client,
            start=ad_input_dto.start,
            end=ad_input_dto.end,
            investment=ad_input_dto.investment
        )
        ad_entry_class.from_model.assert_called_once_with(ad)
        assert ad_entry_class.from_model() == result

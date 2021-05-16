import pytest
from peewee import SqliteDatabase
import src

from src.repositories.adrepository import AdRepository


class TestData:

    def test_class_att_database(self):
        assert isinstance(src.repositories.adrepository.AdRepository.database, SqliteDatabase)

    def test_get_or_create_ad(self, mocker, ad_input):
        ad_entry_class = mocker.patch('src.repositories.adrepository.AdEntryDTO')

        ad_class = mocker.patch('src.repositories.adrepository.Ad')
        ad = mocker.Mock()
        ad_class.get_or_create.return_value = ad, mocker.Mock()

        data = AdRepository()
        result = data.get_or_create_ad.__wrapped__(data, ad_input)

        ad_class.get_or_create.assert_called_once_with(
            name=ad_input.name,
            client=ad_input.client,
            start=ad_input.start,
            end=ad_input.end,
            investment=ad_input.investment
        )
        ad_entry_class.from_model.assert_called_once_with(ad)
        assert ad_entry_class.from_model() == result

    def test_find_all_ads(self, mocker):
        ad_entry_class = mocker.patch('src.repositories.adrepository.AdEntryDTO')
        ad_class = mocker.patch('src.repositories.adrepository.Ad')

        query_result = [mocker.Mock() for i in range(5)]
        ad_class.select.return_value = query_result

        data = AdRepository()
        result = data.find_all_ads.__wrapped__(data)

        ad_class.select.assert_called_once()

        # Map Ad instances to AdEntryDTO
        from_model_calls_args = [call[0][0] for call in ad_entry_class.from_model.call_args_list]
        for m in query_result:
            assert m in from_model_calls_args

        # Return AdEntryDTO list
        assert result == [ad_entry_class.from_model() for i in range(5)]

    def test_find_ads_by_client(self, mocker, report_input_dto):
        ad_entry_class = mocker.patch('src.repositories.adrepository.AdEntryDTO')
        ad_class = mocker.patch('src.repositories.adrepository.Ad')

        query_result = [mocker.Mock() for i in range(5)]
        ad_class.select.return_value.where.return_value = query_result

        data = AdRepository()
        result = data.find_ads_by_client.__wrapped__(data, report_input_dto)

        ad_class.select().where.assert_called_once()

        # Map Ad instances to AdEntryDTO
        from_model_calls_args = [call[0][0] for call in ad_entry_class.from_model.call_args_list]
        for m in query_result:
            assert m in from_model_calls_args

        # Return AdEntryDTO list
        assert result == [ad_entry_class.from_model() for i in range(5)]

    def test_find_ads_by_period(self, mocker, report_input_dto):
        select_spy = mocker.spy(src.repositories.adrepository.Ad, 'select')
        ad_entry_class = mocker.patch('src.repositories.adrepository.AdEntryDTO')

        data = AdRepository()
        result = data.find_ads_by_period.__wrapped__(data, report_input_dto)

        select_spy.assert_called_once()

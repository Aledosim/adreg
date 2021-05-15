from peewee import SqliteDatabase

import src

from src.repositories.adrepository import AdRepository


class TestData:

    def test_class_att_database(self):
        assert isinstance(src.repositories.adrepository.AdRepository.database, SqliteDatabase)

    def test_get_or_create_ad(self, mocker, ad_input_dto):
        mocker.patch('src.repositories.adrepository.AdRepository.database')
        ad_entry_class = mocker.patch('src.repositories.adrepository.AdEntryDTO')

        ad_class = mocker.patch('src.repositories.adrepository.Ad')
        ad = mocker.Mock()
        ad_class.get_or_create.return_value = ad, mocker.Mock()

        data = AdRepository()
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

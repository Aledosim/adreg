import pytest

import src
from .fixtures.ad_dto import ad_dto

from src.business import AdReg


class TestAdReg:
    def test_init(self, mocker):
        mocker.patch('src.business.Data')
        data_class = src.business.Data

        AdReg()

        data_class.assert_called_once()

    def test_create_adreg(self, mocker, ad_dto):
        mocker.patch('src.business.Data')

        adreg = AdReg()
        result = adreg.create_adreg(ad_dto)

        adreg.data.get_or_create_entry.assert_called_once_with(ad_dto)
        assert adreg.data.get_or_create_entry() == result

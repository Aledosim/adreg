import src

from src.business import AdReg


class TestAdReg:
    def test_init(self, mocker):
        mocker.patch('src.business.AdRepository')
        data_class = src.business.AdRepository

        AdReg()

        data_class.assert_called_once()

    def test_create_adreg(self, mocker, ad_input_dto):
        mocker.patch('src.business.AdRepository')

        adreg = AdReg()
        result = adreg.create_adreg(ad_input_dto)

        adreg.data.get_or_create_ad.assert_called_once_with(ad_input_dto)
        assert adreg.data.get_or_create_ad() == result

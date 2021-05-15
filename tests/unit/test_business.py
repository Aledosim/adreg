import src

from src.business import AdReg


class TestAdReg:
    def test_init(self, mocker):
        mocker.patch('src.business.AdRepository')
        data_class = src.business.AdRepository

        AdReg()

        data_class.assert_called_once()

    def test_create_adreg(self, mocker, ad_input):
        mocker.patch('src.business.AdRepository')

        adreg = AdReg()
        result = adreg.create_adentry(ad_input)

        adreg.data.get_or_create_ad.assert_called_once_with(ad_input)
        assert adreg.data.get_or_create_ad() == result

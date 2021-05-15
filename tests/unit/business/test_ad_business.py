import src

from src.business.adbusiness import AdReg


class TestAdReg:
    def test_init(self, mocker):
        mocker.patch('src.business.adbusiness.AdRepository')
        data_class = src.business.adbusiness.AdRepository

        AdReg()

        data_class.assert_called_once()

    def test_create_adreg(self, mocker, ad_input_dto):
        mocker.patch('src.business.adbusiness.AdRepository')

        adreg = AdReg()
        result = adreg.create_adentry(ad_input_dto)

        adreg.data.get_or_create_ad.assert_called_once_with(ad_input_dto)
        assert adreg.data.get_or_create_ad() == result

    def test_create_report(self, mocker, report_input_dto):
        mocker.patch('src.business.adbusiness.AdRepository')

        adreg = AdReg()
        result = adreg.create_report(report_input_dto)


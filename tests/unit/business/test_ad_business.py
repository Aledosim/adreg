import pytest
import src

from src.business.adbusiness import AdReg, calculate_total


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

    def test_create_generic_report(self, mocker, report_input_dto, ad_entry_dto):
        ad_repository_mock = mocker.patch('src.business.adbusiness.AdRepository')
        report_dto_mock = mocker.patch('src.business.adbusiness.ReportDTO')
        calculate_total_mock = mocker.patch('src.business.adbusiness.calculate_total')
        calculate_total_mock.return_value = 16000, 11200, 1344, 192,

        report_input_dto.client = None
        report_input_dto.start = None

        entries = [ad_entry_dto for i in range(5)]
        ad_repository_mock().find_all_ads.return_value = entries

        adreg = AdReg()
        result = adreg.create_report(report_input_dto)

        adreg.data.find_ads_by_client.assert_not_called()
        adreg.data.find_ads_by_period.assert_not_called()
        adreg.data.find_ads_by_client_and_period.assert_not_called()

        adreg.data.find_all_ads.assert_called_once()

        # calculate total per entry
        calculate_total_calls_args = [call[0][0] for call in calculate_total_mock.call_args_list]
        for m in entries:
            assert m in calculate_total_calls_args

        # Return list of ReportDTO
        assert result == [report_dto_mock.from_ad_entry() for i in range(5)]

    def test_create_client_report(self, mocker, report_input_dto, ad_entry_dto):
        ad_repository_mock = mocker.patch('src.business.adbusiness.AdRepository')
        report_dto_mock = mocker.patch('src.business.adbusiness.ReportDTO')
        calculate_total_mock = mocker.patch('src.business.adbusiness.calculate_total')
        calculate_total_mock.return_value = 16000, 11200, 1344, 192,

        entries = [ad_entry_dto for i in range(5)]
        ad_repository_mock().find_ads_by_client.return_value = entries

        report_input_dto.start = None

        adreg = AdReg()
        result = adreg.create_report(report_input_dto)

        adreg.data.find_all_ads.assert_not_called()
        adreg.data.find_ads_by_period.assert_not_called()
        adreg.data.find_ads_by_client_and_period.assert_not_called()

        adreg.data.find_ads_by_client.assert_called_once_with(report_input_dto)

        # calculate total per entry
        calculate_total_calls_args = [call[0][0] for call in calculate_total_mock.call_args_list]
        for m in entries:
            assert m in calculate_total_calls_args

        # Return list of ReportDTO
        assert result == [report_dto_mock.from_ad_entry() for i in range(5)]

    def test_create_period_report(self, mocker, report_input_dto, ad_entry_dto):
        ad_repository_mock = mocker.patch('src.business.adbusiness.AdRepository')
        report_dto_mock = mocker.patch('src.business.adbusiness.ReportDTO')
        calculate_total_mock = mocker.patch('src.business.adbusiness.calculate_total')
        calculate_total_mock.return_value = 16000, 11200, 1344, 192,

        entries = [ad_entry_dto for i in range(5)]
        ad_repository_mock().find_ads_by_period.return_value = entries

        report_input_dto.client = None

        adreg = AdReg()
        result = adreg.create_report(report_input_dto)

        adreg.data.find_all_ads.assert_not_called()
        adreg.data.find_ads_by_client.assert_not_called()
        adreg.data.find_ads_by_client_and_period.assert_not_called()

        adreg.data.find_ads_by_period.assert_called_once_with(report_input_dto)


class TestCalculateTotal:
    def test_calculate_total(self, ad_entry_dto, mocker):
        calculator_mock = mocker.patch('src.business.adbusiness.calculator')
        calculator_mock.return_value = 350, 42, 6,

        n_days = ad_entry_dto.end - ad_entry_dto.start

        result = calculate_total(ad_entry_dto, n_days)

        calculator_mock.assert_called_with(ad_entry_dto.investment)

        assert (16000, 11200, 1344, 192) == result

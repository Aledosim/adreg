from datetime import date
import pytest

@pytest.fixture
def ad_input(mocker):
    ad_dto = mocker.Mock()

    ad_dto.name = 'test name'
    ad_dto.client = 'test client'
    ad_dto.start = '5-4-2021'
    ad_dto.end = '7-5-2021'
    ad_dto.investment = 500

    return ad_dto

@pytest.fixture
def report_input_dto(mocker):
    report_input_dto = mocker.Mock()

    report_input_dto.client = 'test client'
    report_input_dto.start = date(2021, 4, 5)
    report_input_dto.end = date(2021, 5, 7)

    return report_input_dto

@pytest.fixture
def report_dto(report_input_dto):
    report_dto = report_input_dto
    report_dto.total = 16000
    report_dto.max_views = 500
    report_dto.max_clicks = 30

    return report_dto

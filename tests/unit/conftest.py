import pytest

@pytest.fixture
def ad_dto(mocker):
    ad_dto = mocker.Mock()

    ad_dto.name='test name',
    ad_dto.client='test client',
    ad_dto.start='5-4-2021',
    ad_dto.end='7-5-2021',
    ad_dto.investment=500

    return ad_dto

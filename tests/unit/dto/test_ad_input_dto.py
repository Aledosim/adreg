from datetime import date

from src.dto.ad_input import AdInputDTO


class TestAd:
    def test_init(self):
        name = 'test name'
        client = 'test client'
        start = date(2021, 4, 5)
        end = date(2021, 5, 7)
        investment = 500

        ad_dto = AdInputDTO(
            name=name,
            client=client,
            start=start,
            end=end,
            investment=investment
        )

        assert name == ad_dto.name
        assert client == ad_dto.client
        assert start ==  ad_dto.start
        assert end == ad_dto.end
        assert investment == ad_dto.investment
from datetime import date

from src.dto.ad import Ad


class TestAd:
    def test_init(self):
        name = 'test name'
        client = 'test client'
        start = date(2021, 4, 5)
        end = date(2021, 5, 7)
        investment = 500

        ad_dto = Ad(
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

    def test_from_model(self, mocker):
        name = 'test name'
        client = 'test client'
        start = date(2021, 4, 5)
        end = date(2021, 5, 7)
        investment = 500

        model = mocker.Mock()
        model.name = name
        model.client = client
        model.start = start
        model.end = end
        model.investment = investment

        ad_dto = Ad.from_model(model)

        assert isinstance(ad_dto, Ad)
        assert name == ad_dto.name
        assert client == ad_dto.client
        assert start ==  ad_dto.start
        assert end == ad_dto.end
        assert investment == ad_dto.investment

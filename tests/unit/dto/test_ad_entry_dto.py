from datetime import date, datetime

from src.dto.ad_entry import AdEntryDTO


class TestAdEntry:
    def test_init(self):
        name = 'test name'
        client = 'test client'
        start = date(2021, 4, 5)
        end = date(2021, 5, 7)
        investment = 500
        created_at = datetime.now()
        updated_at = datetime.now()
        id = 1

        ad_entry_dto = AdEntryDTO(
            name=name,
            client=client,
            start=start,
            end=end,
            investment=investment,
            created_at=created_at,
            updated_at=updated_at,
            id=id
        )

        assert name == ad_entry_dto.name
        assert client == ad_entry_dto.client
        assert start == ad_entry_dto.start
        assert end == ad_entry_dto.end
        assert investment == ad_entry_dto.investment
        assert created_at == ad_entry_dto.created_at
        assert updated_at == ad_entry_dto.updated_at
        assert id == ad_entry_dto.id

    def test_from_model(self, mocker):
        name = 'test name'
        client = 'test client'
        start = date(2021, 4, 5)
        end = date(2021, 5, 7)
        investment = 500
        created_at = datetime.now()
        updated_at = datetime.now()
        id = 1

        model = mocker.Mock()
        model.name = name
        model.client = client
        model.start = start
        model.end = end
        model.investment = investment
        model.created_at = created_at
        model.updated_at = updated_at
        model.id = id

        ad_entry_dto = AdEntryDTO.from_model(model)

        assert isinstance(ad_entry_dto, AdEntryDTO)
        assert name == ad_entry_dto.name
        assert client == ad_entry_dto.client
        assert start == ad_entry_dto.start
        assert end == ad_entry_dto.end
        assert investment == ad_entry_dto.investment
        assert created_at == ad_entry_dto.created_at
        assert updated_at == ad_entry_dto.updated_at
        assert id == ad_entry_dto.id

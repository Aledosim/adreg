from src.dto.ad_input import AdInputDTO


class AdEntryDTO(AdInputDTO):
    def __init__(self, created_at=None, updated_at=None, id=None, **kwargs):
        super().__init__(**kwargs)
        self.created_at = created_at
        self.updated_at = updated_at
        self.id = id

    @staticmethod
    def from_model(model):
        ad_entry_dto = AdEntryDTO(
            name=model.name,
            client=model.client,
            start=model.start,
            end=model.end,
            investment=model.investment,
            created_at=model.created_at,
            updated_at=model.updated_at,
            id=model.id
        )

        return ad_entry_dto

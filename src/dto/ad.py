
class AdDTO:
    def __init__(self, name=None, client=None, start=None, end=None, investment=None):
        self.name = name
        self.client = client
        self.start = start
        self.end = end
        self.investment = investment

    @staticmethod
    def from_model(model):
        ad = AdDTO(
            name=model.name,
            client=model.client,
            start=model.start,
            end=model.end,
            investment=model.investment
        )

        return ad

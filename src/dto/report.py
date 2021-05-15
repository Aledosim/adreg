from src.dto.report_input import ReportInputDTO

class ReportDTO(ReportInputDTO):
    def __init__(self, total=None, max_views=None, max_clicks=None, max_shares=None, **kwargs):
        super().__init__(**kwargs)
        self.total = total
        self.max_views = max_views
        self.max_clicks = max_clicks
        self.max_shares = max_shares

    @staticmethod
    def from_model(model):
        report_dto = ReportDTO(
            client=model.client,
            start=model.start,
            end=model.end,
            total=model.total,
            max_views=model.max_views,
            max_clicks=model.max_clicks,
            max_shares=model.max_shares,
        )
        return report_dto

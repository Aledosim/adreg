from src.dto.ad_entry import AdEntryDTO


class ReportDTO(AdEntryDTO):
    def __init__(self, total=None, max_views=None, max_clicks=None, max_shares=None, **kwargs):
        super().__init__(**kwargs)
        self.total = total
        self.max_views = max_views
        self.max_clicks = max_clicks
        self.max_shares = max_shares

    @staticmethod
    def from_ad_entry(ad_entry, total=None, max_views=None, max_clicks=None, max_shares=None):
        report_dto = ReportDTO(
            name=ad_entry.name,
            client=ad_entry.client,
            start=ad_entry.start,
            end=ad_entry.end,
            investment=ad_entry.investment,
            created_at=ad_entry.created_at,
            updated_at=ad_entry.updated_at,
            id=ad_entry.id,
            total=total,
            max_views=max_views,
            max_clicks=max_clicks,
            max_shares=max_shares,
        )

        return report_dto

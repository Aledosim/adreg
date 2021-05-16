import pytest
from src.dto.report import ReportDTO

class TestReportDTO:
    def test_init(self, report_dto):

        report_dto_obj = ReportDTO(
            client=report_dto.client,
            start=report_dto.start,
            end=report_dto.end,
            total=report_dto.total,
            max_views=report_dto.max_views,
            max_clicks=report_dto.max_clicks,
            max_shares=report_dto.max_shares,
        )

        assert report_dto_obj.client == report_dto.client
        assert report_dto_obj.start == report_dto.start
        assert report_dto_obj.end == report_dto.end
        assert report_dto_obj.total == report_dto.total
        assert report_dto_obj.max_views == report_dto.max_views
        assert report_dto_obj.max_clicks == report_dto.max_clicks
        assert report_dto_obj.max_shares == report_dto.max_shares

    @pytest.mark.only
    def test_from_ad_entry(self, ad_entry_dto, report_dto):
        report_dto_obj = ReportDTO.from_ad_entry(
            ad_entry_dto,
            total=report_dto.total,
            max_views=report_dto.max_views,
            max_clicks=report_dto.max_clicks,
            max_shares=report_dto.max_shares,
        )

        assert isinstance(report_dto_obj, ReportDTO)
        assert report_dto_obj.name == ad_entry_dto.name
        assert report_dto_obj.client == ad_entry_dto.client
        assert report_dto_obj.start == ad_entry_dto.start
        assert report_dto_obj.end == ad_entry_dto.end
        assert report_dto_obj.investment == ad_entry_dto.investment
        assert report_dto_obj.created_at == ad_entry_dto.created_at
        assert report_dto_obj.updated_at == ad_entry_dto.updated_at
        assert report_dto_obj.id == ad_entry_dto.id

        assert report_dto_obj.total == report_dto.total
        assert report_dto_obj.max_views == report_dto.max_views
        assert report_dto_obj.max_clicks == report_dto.max_clicks
        assert report_dto_obj.max_shares == report_dto.max_shares



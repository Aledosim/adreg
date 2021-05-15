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

    def test_from_model(self, mocker, report_dto):

        model = mocker.Mock()
        model.client=report_dto.client
        model.start=report_dto.start
        model.end=report_dto.end
        model.total=report_dto.total
        model.max_views=report_dto.max_views
        model.max_clicks=report_dto.max_clicks
        model.max_shares=report_dto.max_shares

        report_dto_obj = ReportDTO.from_model(model)

        assert isinstance(report_dto_obj, ReportDTO)
        assert report_dto_obj.client == report_dto.client
        assert report_dto_obj.start == report_dto.start
        assert report_dto_obj.end == report_dto.end
        assert report_dto_obj.total == report_dto.total
        assert report_dto_obj.max_views == report_dto.max_views
        assert report_dto_obj.max_clicks == report_dto.max_clicks
        assert report_dto_obj.max_shares == report_dto.max_shares


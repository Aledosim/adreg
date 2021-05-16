from src.dto.report_input import ReportInputDTO


class TestReportInputDTO:
    def test_init(self, report_input_dto):

        report_input_dto_obj = ReportInputDTO(
            client=report_input_dto.client,
            start=report_input_dto.start,
            end=report_input_dto.end
        )

        assert report_input_dto_obj.client == report_input_dto.client
        assert report_input_dto_obj.start == report_input_dto.start
        assert report_input_dto_obj.end == report_input_dto.end

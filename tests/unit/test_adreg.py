import argparse
import sys

import adreg

from adreg import main, add, report, create_add_subparser, create_report_subparser, print_report


class TestMain:
    def test_create_parsers(self, mocker):
        mocker.patch('argparse.ArgumentParser')
        mocker.patch('adreg.create_add_subparser')
        mocker.patch('adreg.create_report_subparser')

        main()

        adreg.create_add_subparser.assert_called_once()
        adreg.create_report_subparser.assert_called_once()

    def test_print_help_and_exit_when_no_args(self, mocker):
        mocker.patch('sys.exit')
        mocker.patch('adreg.vars').return_value = {}
        mocker.patch('argparse.ArgumentParser')
        arg_parser = argparse.ArgumentParser()

        main()

        arg_parser.print_help.assert_called_once()
        sys.exit.assert_called_once()

    def test_call_func_of_argument(self, mocker):
        mocker.patch('argparse.ArgumentParser')
        args = argparse.ArgumentParser().parse_args()

        main()

        args.func.assert_called_once_with(args)


class TestCreateAddSubparser:
    def test_create_add_subparser(self, mocker):
        add_mock = mocker.patch('adreg.add')
        mock_parser = mocker.Mock()
        mock_parser.add_parser = mocker.Mock(return_value=mock_parser)

        create_add_subparser(mock_parser)

        mock_parser.add_parser.assert_called_once()
        assert 'add' in mock_parser.add_parser.call_args[0]

        mock_parser.add_parser().set_defaults.assert_called_once_with(func=add_mock)

        # Assert the first argument of all add_argument calls
        arg_list = [call[0][0] for call in mock_parser.add_argument.call_args_list]
        assert 5 == len(arg_list)
        assert '--name' in arg_list
        assert '--client' in arg_list
        assert '--start' in arg_list
        assert '--end' in arg_list
        assert '--investment' in arg_list


class TestCreateReportSubparser:
    def test_create_report_parser(self, mocker):
        report_mock = mocker.patch('adreg.report')
        mock_parser = mocker.Mock()
        mock_parser.add_parser = mocker.Mock(return_value=mock_parser)

        create_report_subparser(mock_parser)

        mock_parser.add_parser.assert_called_once()
        assert 'report' in mock_parser.add_parser.call_args[0]

        mock_parser.add_parser().set_defaults.assert_called_once_with(func=report_mock)

        # Assert the first argument of all add_argument calls
        arg_list = [call[0][0] for call in mock_parser.add_argument.call_args_list]
        assert 3 == len(arg_list)
        assert '--client' in arg_list
        assert '--start' in arg_list
        assert '--end' in arg_list


class TestAdd:
    def test_add_function_passes_correct_arguments(self, ad_input, mocker):
        service = mocker.patch('adreg.AdService')
        args = ad_input

        add(args)

        service.assert_called_once()
        service().add.assert_called_with(
            name=args.name,
            client=args.client,
            start=args.start,
            end=args.end,
            investment=args.investment * 100,
        )


class TestReport:
    def test_report_function(self, report_input, report_dto, mocker):
        mocker.patch('adreg.print_report')
        service = mocker.patch('adreg.AdService')

        report_list = [report_dto for i in range(5)]
        service.return_value.report.return_value = report_list

        args = report_input
        report(args)

        service.assert_called_once()
        service().report.assert_called_with(
            client=args.client,
            start=args.start,
            end=args.end,
        )

        adreg.print_report.assert_called_once_with(report_list)


class TestPrintReport:
    def test_print_report(self, report_dto, mocker):
        mocker.patch('adreg.format_report')
        mocker.patch('adreg.map')
        tabulate_mock = mocker.patch('adreg.tabulate')

        reports = [report_dto for i in range(5)]

        print_report(reports)

        adreg.map.assert_called_once_with(adreg.format_report, reports)

        tabulate_mock.assert_called_once()

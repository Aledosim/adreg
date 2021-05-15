import pytest
import subprocess
import argparse
import sys

import adreg

from adreg import main, add, create_add_subparser, create_report_subparser


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
        mock_parser = mocker.Mock()
        mock_parser.add_parser = mocker.Mock(return_value=mock_parser)

        create_add_subparser(mock_parser)

        mock_parser.add_parser.assert_called_once()
        assert 'add' in mock_parser.add_parser.call_args[0]

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
        mock_parser = mocker.Mock()
        mock_parser.add_parser = mocker.Mock(return_value=mock_parser)

        create_report_subparser(mock_parser)

        mock_parser.add_parser.assert_called_once()
        assert 'report' in mock_parser.add_parser.call_args[0]

        # Assert the first argument of all add_argument calls
        arg_list = [call[0][0] for call in mock_parser.add_argument.call_args_list]
        assert 3 == len(arg_list)
        assert '--client' in arg_list
        assert '--start' in arg_list
        assert '--end' in arg_list


class TestAdd:
    def test_add_function_passes_correct_arguments(self, mocker):
        mocker.patch('adreg.AdService')

        name = 'test name'
        client = 'test client'
        start = '5-4-2021'
        end = '7-5-2021'
        investment = 500

        args = mocker.MagicMock()
        args.name = name
        args.client = client
        args.start = start
        args.end = end
        args.investment = investment

        add(args)

        adreg.AdService().add.assert_called_with(
            name=name,
            client=client,
            start=start,
            end=end,
            investment=investment
        )

import pytest
import subprocess

import adreg
import argparse

from adreg import main, add, create_add_subparser


class TestMain:
    def test_create_parsers(self, mocker):
        mocker.patch('argparse.ArgumentParser')
        mocker.patch('adreg.create_add_subparser')

        main()

        adreg.create_add_subparser.assert_called_once()

        # TODO test if main call args.func

class TestAdd:
    def test_create_add_parser(self, mocker):
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

    def test_add_function_passes_correct_arguments(self, mocker):
        mocker.patch('adreg.Ad')

        args = mocker.MagicMock()
        args.name = 'test name',
        args.client = 'test client',
        args.start = '5-4-2021',
        args.end = '7-5-2021',
        args.investment = 500

        add(args)

        adreg.Ad().add.assert_called_with(
            name='test name',
            client='test client',
            start='5-4-2021',
            end='7-5-2021',
            investment=500
        )

import subprocess
import pytest
from src.data import Data

def test_first_record(mocker, get_models):
    models = get_models(Data.models)

    # Eli is a happy employee of Divulga Tudo
    # He wants to use the brand new system of advertisement registry

    # First he tries to run the command only
    result = subprocess.run(['./adreg'], capture_output=True )

    assert result.returncode == 0
    # He reads the help information
    # with open('tests/fixtures/help_main') as help_file:
    #     assert help_file.read() == result.stdout

    # then try to add a new record, but with a typo
    result = subprocess.run([
        './adreg', 'add',
        '-n', 'especial de natal',
        '-c', 'porta dos fundos',
        '-i', '1-12-2020',
        '-e', '25-12-2020',
        '-i', '20000'
    ])

    assert result.returncode == 2

    # after he reads the error output, he correct the command
    # assert result.stderr == 'some error'

    result = subprocess.run([
        './adreg', 'add',
        '-n', 'especial de natal',
        '-c', 'porta dos fundos',
        '-s', '1-12-2020',
        '-e', '25-12-2020',
        '-i', '20000'
    ])

    # and it succeed
    assert result.returncode == 0
    models['Ad'].get(name='especial de natal')

    # Satisfied he reads the success output
    # assert result.stdout == 'success text'

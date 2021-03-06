import subprocess
from src.database import models as db_models


def test_first_record(get_models):
    models = get_models(db_models)

    # Eli is a happy employee of Divulga Tudo
    # He wants to use the brand new system of advertisement registry

    # First he tries to run the command only
    result = subprocess.run(['./adreg'], text=True, capture_output=True)

    assert result.returncode == 0
    # He reads the help information
    with open('tests/outputs/main_help') as help_file:
        assert help_file.read() == result.stdout

    # then try to add a new record, but with a typo
    result = subprocess.run([
        './adreg', 'add',
        '-n', 'especial de natal',
        '-c', 'porta dos fundos',
        '-i', '1-12-2020',
        '-e', '25-12-2020',
        '-i', '200.00'
    ], text=True, capture_output=True)

    assert result.returncode == 2

    # after he reads the error output, he correct the command
    with open('tests/outputs/typo_out') as typo_file:
        assert typo_file.read() == result.stderr

    result = subprocess.run([
        './adreg', 'add',
        '-n', 'especial de natal',
        '-c', 'porta dos fundos',
        '-s', '1-12-2020',
        '-e', '25-12-2020',
        '-i', '200.00'
    ])

    # and it succeed
    assert result.returncode == 0
    models['Ad'].get(name='especial de natal')  # throws AdDoesNotExist if entry is not present

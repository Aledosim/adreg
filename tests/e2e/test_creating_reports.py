import pytest
import subprocess


def test_client_report(apply_test_db):
    # Eli have a new task, to make a report on advertises
    # First he reads the help text
    result = subprocess.run([
        './adreg', 'report',
        '--help'
    ])

    assert result.returncode == 0
    # with open() as help_report:
    #     assert result.stdout == help_report.read()

    # Just for curiosity, Eli requests all reports
    result = subprocess.run([
        './adreg', 'report',
    ])

    assert result.returncode == 0
    # assert result.stdout == ''

    # ... all reports of Porta dos Fundos
    result = subprocess.run([
        './adreg', 'report',
        '--client', 'porta dos fundos'
    ])

    assert result.returncode == 0
    # assert result.stdout == ''

    # ... and any Christmas campaign
    result = subprocess.run([
        './adreg', 'report',
        '--start', '11-12-2020',
        '--end', '26-12-2020'
    ])

    assert result.returncode == 0
    # assert result.stdout == ''

    # But he really wants Rocketseat late april results
    result = subprocess.run([
        './adreg', 'report',
        '--client', 'rocketseat',
        '--start', '15-4-2021',
        '--end', '30-4-2021'
    ])

    assert result.returncode == 0
    # assert result.stdout == ''

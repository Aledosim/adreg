import subprocess

def test_first_record():
    # Eli is a happy employee of Divulga Tudo
    # He wants to use the brand new system of advertisement registry

    # First he tries to run the command only
    result = subprocess.run(['adreg'])

    # He reads the help information
    with open('tests/fixtures/help_main') as help_file:
        assert help_file.read() == result.stdout

    # then try to add a new record, but with a typo
    result = subprocess.run([
        'adreg', 'add',
        '-n', 'especial de natal',
        '-c', 'porta dos fundos',
        '-i', '1-12-2020',
        '-e', '25-12-2020',
        '-i', '20000'
    ])

    # after he reads the error output, he correct the command

    # Satisfied he reads the success output

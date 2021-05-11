import subprocess

class TestAdd:

    def test_user_interface(self):
        cmd = [
            'python',
            'adreg/presentation.py',
            'add',
            '--name', 'test name',
            '--client', 'test client',
            '--start', '2-3-2021',
            '--end', '10-3-2021',
            '--investment', '500'
        ]
        result = subprocess.run(cmd)
        print(result.stdout)
        print(result.stderr)

        assert result.returncode == 0

        #TODO Test if the ad is correctly added to database

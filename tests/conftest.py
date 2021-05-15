from pathlib import Path
import tempfile
import os


def set_env():
    test_dir = Path(tempfile.mkdtemp())
    test_file = test_dir.joinpath('test.db')

    os.environ['ADREG_TEST_DB'] = str(test_file)


def pytest_sessionstart():
    set_env()


def pytest_runtest_setup(item):
    set_env()
    item.setup()


def pytest_runtest_teardown(item):
    if 'ADREG_TEST_DB' in os.environ:
        del os.environ['ADREG_TEST_DB']

    item.teardown()

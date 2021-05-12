import pytest
from dicttoobject import dict_to_readonly_object
from schema import SchemaError
from yaml import dump

from src.configs import get_configs


class TestConfig:

    def test_create_object_from_yaml_file(self, tmp_path):
        test_config = {
            'DATABASE_DIR': 'path/to/dir'
        }
        with open(tmp_path.joinpath('configs.yml'), 'w') as _configs:
            dump(test_config, _configs)

        configs = get_configs(tmp_path)

        assert configs == dict_to_readonly_object(test_config)

    def test_pass_invalid_config(self, tmp_path):
        test_config = {'INVALID': 'path/to/dir'}
        with open(tmp_path.joinpath('configs.yml'), 'w') as _configs:
            dump(test_config, _configs)

        with pytest.raises(SchemaError):
            get_configs(tmp_path)


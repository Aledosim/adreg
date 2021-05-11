from yaml import full_load
from schema import Schema
from dicttoobject import dict_to_readonly_object

schema = Schema(
    {
        'DATABASE_DIR': str,
    }
)

def get_configs(config_path='.'):
    with open(config_path.joinpath('configs.yml')) as config_file:
        configs = full_load(config_file)

    schema.validate(configs)
    return dict_to_readonly_object(configs)

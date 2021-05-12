from schema import Schema, Regex, And
from datetime import datetime

from src.business import add_reg

add_schema = Schema({
    'name': And(str, error='name must be str'),
    'client': And(str, error='client must be str'),
    'start': And(
        And(str, error='start date must be str'),
        Regex(r'[0-9]{1,2}-[0-9]{1,2}-[0-9]{4}', error='start date must be in the format dd-mm-yyyy')
    ),
    'end': And(
        And(str, error='end date must be str'),
        Regex(r'[0-9]{1,2}-[0-9]{1,2}-[0-9]{4}', error='end date must be in the format dd-mm-yyyy')
    ),
    'investment': And(
        And(int, error='investment must be int'),
        And(lambda n: n >0, error='investment must be positive'),
    )
})

def add_ad(name=None, client=None, start=None, end=None, investment=None):
    add_schema.validate({
        'name': name,
        'client': client,
        'start': start,
        'end': end,
        'investment': investment,
    })

    add_reg(
        name=name,
        client=client,
        start=datetime.strptime(start, '%d-%m-%Y').date(),
        end=datetime.strptime(end, '%d-%m-%Y').date(),
        investment=investment
    )

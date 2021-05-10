from datetime import datetime

import pytest
from peewee import Model
from peewee import BinaryUUIDField, DateTimeField


@pytest.fixture
def mock_model():

    class MockModel(Model):
        id = BinaryUUIDField(primary_key=True)
        created_at = DateTimeField(default=datetime.now())
        updated_at = DateTimeField(default=datetime.now())

    return MockModel

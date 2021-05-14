import pytest
from peewee import Model
import src

from src.models.ad import Ad

def test_ad_attributes(mocker):
    mocker.patch('src.models.ad.CharField')
    mocker.patch('src.models.ad.DateField')
    mocker.patch('src.models.ad.IntegerField')
    mocker.patch('src.models.ad.DateTimeField')
    mocker.patch('src.models.ad.AutoField')

    assert issubclass(Ad, Model)
    assert Ad.name == src.models.ad.CharField()
    assert Ad.client == src.models.ad.CharField()
    assert Ad.start == src.models.ad.DateField()
    assert Ad.end == src.models.ad.DateField()
    assert Ad.investment == src.models.ad.IntegerField()
    assert Ad.created_at == src.models.ad.DateTimeField()
    assert Ad.updated_at == src.models.ad.DateTimeField()
    assert Ad.id == src.models.ad.AutoField()

import src
from src.models.base import BaseModel

from src.models.ad import Ad

def test_ad_attributes(mocker):
    mocker.patch('src.models.ad.CharField')
    mocker.patch('src.models.ad.DateField')
    mocker.patch('src.models.ad.IntegerField')

    assert issubclass(Ad, BaseModel)
    assert Ad.name == src.models.ad.CharField()
    assert Ad.client == src.models.ad.CharField()
    assert Ad.start == src.models.ad.DateField()
    assert Ad.end == src.models.ad.DateField()
    assert Ad.investment == src.models.ad.IntegerField()

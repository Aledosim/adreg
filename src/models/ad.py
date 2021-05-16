from peewee import CharField, DateField, IntegerField

from src.models.base import BaseModel


class Ad(BaseModel):
    name = CharField()
    client = CharField()
    start = DateField()
    end = DateField()
    investment = IntegerField()

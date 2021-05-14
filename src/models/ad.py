from peewee import Model, CharField, DateField, IntegerField, DateTimeField, AutoField
from datetime import datetime


class Ad(Model):
    name = CharField()
    client = CharField()
    start = DateField()
    end = DateField()
    investment = IntegerField()
    created_at = DateTimeField(default=datetime.now())
    updated_at = DateTimeField(default=datetime.now())
    id = AutoField(unique=True, primary_key=True)


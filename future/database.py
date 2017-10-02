# -*- coding:utf-8 -*-

from peewee import Model
from peewee_async import Manager
from peewee_async import PostgresqlDatabase

from future import CONFIG

DB_CONFIG = CONFIG.DB_CONFIG
database = PostgresqlDatabase(**DB_CONFIG)

objects = Manager(database)


class BaseModel(Model):
    class Meta:
        database = database

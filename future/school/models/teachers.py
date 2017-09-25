# -*- coding: utf-8 -*-

from peewee import Model
from peewee import FixedCharField


class Teachers(Model):
    name = FixedCharField()

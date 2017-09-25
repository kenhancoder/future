# -*- coding: utf-8 -*-

from peewee import FixedCharField
from future.database import BaseModel


class Teachers(BaseModel):

    name = FixedCharField(verbose_name='Teacher Name')

    def __str__(self):
        return self.name

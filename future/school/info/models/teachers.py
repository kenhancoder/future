# -*- coding: utf-8 -*-

from peewee import FixedCharField

from future.database import BaseModel


class Teachers(BaseModel):

    name = FixedCharField(verbose_name='Teacher Name')

    def __str__(self):
        return self.name

    @classmethod
    def get_all(cls):
        result = {}
        result['teacherls'] = []
        ls = cls.select()
        return [{'name': item.name, 'id': item.id} for item in ls]

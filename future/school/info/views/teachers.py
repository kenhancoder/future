# -*- coding: utf-8 -*-

from sanic.views import HTTPMethodView
from marshmallow_peewee import ModelSchema

from ..models.teachers import Teachers


class TeacherSchema(ModelSchema):

    class Meta:
        model = Teachers


class TeacherListView(HTTPMethodView):

    async def get(self, request):
        return Teachers.get_all()

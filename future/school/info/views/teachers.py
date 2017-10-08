# -*- coding: utf-8 -*-

from sanic.views import HTTPMethodView
from marshmallow_peewee import ModelSchema

from ..models.teachers import Teachers
from future.marshal import marshal_with


class TeacherSchema(ModelSchema):

    class Meta:
        model = Teachers

    validate = False


class TeacherListView(HTTPMethodView):

    @marshal_with(TeacherSchema)
    async def get(self, request):
        return Teachers.get_all()

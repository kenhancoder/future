# -*- coding: utf-8 -*-

from sanic import Blueprint

from .info import TeacherListView

bp_v1 = Blueprint('api', url_prefix='/api/v1')

bp_v1.add_route(TeacherListView.as_view(), '/teachers')

# -*- coding: utf-8 -*-

from sanic import Sanic

app = Sanic()


def create_app():

    app = Sanic(__name__)

    return app

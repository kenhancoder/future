# -*- coding: utf-8 -*-

from sanic import Sanic
from future.configs import DevConfig

app = Sanic()


def create_app(config_object=DevConfig):

    app = Sanic(__name__)

    return app

# -*- coding: utf-8 -*-

from sanic.server import HttpProtocol
from sanic.response import text, json


class JSONHttpProtocol(HttpProtocol):

    def write_response(self, response):
        if isinstance(response, str):
            response = text(response)
        elif isinstance(response, (list, dict)):
            response = {'data': response}
        if isinstance(response, dict):
            response = json(response)

        return super().write_response(response)

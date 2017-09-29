# -*- coding: utf-8 -*-

from functools import wraps


def marshal(data, schema):

    if isinstance(data, (list, tuple)):
        return [marshal(d, schema) for d in data]

    result, errors = schema.dump(data)
    if errors:
        for item in errors.items():
            print('{}: {}'.format(*item))
    return result


class marshal_with(object):
    def __init__(self, schema):
        self.schema = schema

    def __call__(self, f):
        @wraps(f)
        async def wrapper(*args, **kwargs):
            resp = await f(*args, **kwargs)
            return marshal(resp, self.schema)
        return wrapper

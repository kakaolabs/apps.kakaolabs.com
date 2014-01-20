import functools

from .serializer import Serializer

def serializer(fields=None):
    def _decl(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            s = Serializer(fields=fields)
            data = s.serialize(res)
            return data
        return wrapper
    return _decl

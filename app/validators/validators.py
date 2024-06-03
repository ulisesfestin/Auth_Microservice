from flask import jsonify, request
from functools import wraps

from marshmallow import ValidationError

def validate_with(schema):
    """
    Se encarga de validar el request con el schema que recibe por parámetro.
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                data = schema().load(request.json)
            except ValidationError as err:
                return jsonify(err.messages), 400
            return f(data, *args, **kwargs)
        return decorated_function
    return decorator

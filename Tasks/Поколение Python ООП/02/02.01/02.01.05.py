# Реализуйте декоратор @jsonify, преобразующий возвращаемое значение декорируемой функции в строку формата JSON.

from functools import wraps
import json


def jsonify(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        new_func = func(*args, **kwargs)
        return json.dumps(new_func)
    return wrapper

from functools import wraps
from typing import Callable
from flask import request

from app.constants import CREATE_TABLE
from app.models import DatabaseConnector

def verify_keys(expected_keys: list):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            body_req = request.get_json()
            invalid_keys = set(expected_keys).difference(body_req)

            try:
                if invalid_keys:
                    raise KeyError(
                        {
                            "error": "wrong key(s)",
                            "expected": list(expected_keys),
                            "received": list(body_req),
                        }
                    )
                return func(*args, **kwargs)
            except (KeyError, TypeError) as e:
                return e.args[0], 400

        return wrapper

    return decorator


def create_table():
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):

            db = DatabaseConnector
            db.get_conn_cur()
            db.cur.execute(CREATE_TABLE)
            db.conn.commit()
            db.cur.close()
            db.conn.close()

            return func(*args, **kwargs)
        return wrapper
    return decorator
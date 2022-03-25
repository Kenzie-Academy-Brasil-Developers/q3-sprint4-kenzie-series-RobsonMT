from http import HTTPStatus
from flask import jsonify, request
from psycopg2.errors import UniqueViolation

from app.constants import EXPECTED_KEYS, SERIE_COLUMNS
from app.decorators import create_table, verify_keys
from app.models.serie_model import Serie


@create_table()
def series():
    series = Serie.read_series()

    serialized_series = [dict(zip(SERIE_COLUMNS, serie)) for serie in series]

    return jsonify(serialized_series), HTTPStatus.OK


@create_table()
@verify_keys(EXPECTED_KEYS)
def create():
    data = request.get_json()

    serie = Serie(**data)
    try:
        inserted_serie = serie.create_new()
    except UniqueViolation:
        return {"error": "serie already exists"}, HTTPStatus.UNPROCESSABLE_ENTITY

    serialized_serie = dict(zip(SERIE_COLUMNS, inserted_serie))

    return serialized_serie, HTTPStatus.CREATED


@create_table()
def select_by_id(serie_id : int):
    serie = Serie.read_by_id(serie_id)
    
    try:
        serialized_serie = dict(zip(SERIE_COLUMNS, serie))
    except TypeError:
        return {}, HTTPStatus.NOT_FOUND

    return {"data": serialized_serie}, HTTPStatus.OK



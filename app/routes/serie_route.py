from flask import Blueprint, Flask
from app.controllers import serie_controller

bp = Blueprint("series", __name__)

bp.get("/series")(serie_controller.series)
bp.post("/series")(serie_controller.create)
bp.get("/series/<int:serie_id>")(serie_controller.select_by_id)
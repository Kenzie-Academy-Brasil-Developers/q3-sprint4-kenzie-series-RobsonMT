from flask import Flask

from .serie_route import bp

def init_app(app: Flask):
    app.register_blueprint(bp)
import os
import logging
from configparser import ConfigParser
from flask import Flask
from flask_smorest import Api
from utils import create_init_db
# from psycopg_pool import ConnectionPool
from stocks.stocks import stocks_bp as StockBlueprint
from stocknews.stocknews import stocknews_bp as StockNewsBlueprint
from indicators.indicators import indicators_bp as IndicatorsBlueprint
def create_app(db_url = None):

    create_init_db()
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stocks REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    # db.init_app(app)
    api = Api(app)
    # with app.app_context():
    #     db.create_all()
    api.register_blueprint(StockNewsBlueprint)
    api.register_blueprint(StockBlueprint)
    api.register_blueprint(IndicatorsBlueprint)

    return app


create_app()
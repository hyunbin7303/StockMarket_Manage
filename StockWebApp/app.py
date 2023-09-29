from configparser import ConfigParser
from flask import Flask
from flask_smorest import Api
from utils import create_init_db
from routes.stocks import stocks_bp as StockBlueprint
from routes.stocknews import stocknews_bp as StockNewsBlueprint
from routes.indicators import indicators_bp as IndicatorsBlueprint
from routes.indicatordata import indicatordata_bp as IndicatordataBlueprint
from di.container import Container
import routes
from repositories.stocksRepository import StocksRepository

def create_app(db_url = None) -> Flask:
    create_init_db()
    container = Container()
    container.wire(modules=[routes.stocks])
    container.wire(modules=[routes.stocknews])
    container.wire(modules=[routes.indicators])
    container.wire(modules=[routes.indicatordata])

    app = Flask(__name__)
    app.container = container

    # test = container.stock_repo.get_all()
    # container.init_resources()
    # stock_repo = container.stock_repo()
    # test = stock_repo.get_all()

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stocks REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    api = Api(app)

    api.register_blueprint(StockNewsBlueprint)
    api.register_blueprint(StockBlueprint)
    api.register_blueprint(IndicatorsBlueprint)
    api.register_blueprint(IndicatordataBlueprint)
    return app


create_app()
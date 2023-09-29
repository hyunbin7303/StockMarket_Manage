from dependency_injector import containers, providers
from repositories.stocksRepository import StocksRepository
from repositories.stocknews_repository import StocknewsRepository
from repositories.indicators_repository import IndicatorsRepository
from repositories.indicatordata_repository import IndicatordataRepository
from dbaccess import Database
from utils import db_conn_string

class Container(containers.DeclarativeContainer):
    Database.initialize(db_conn_string())
    _db_session = Database()
    stock_repo = providers.Factory(StocksRepository, session=_db_session)
    stocknews_repo = providers.Factory(StocknewsRepository, session = _db_session)
    indicators_repo = providers.Factory(IndicatorsRepository, session = _db_session)
    indicatordata_repo = providers.Factory(IndicatordataRepository, session = _db_session)
    
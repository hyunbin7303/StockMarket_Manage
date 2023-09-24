from dependency_injector import containers, providers
from repositories.stocksRepository import StocksRepository
from dbaccess import Database
from utils import db_conn_string

class Container(containers.DeclarativeContainer):
    Database.initialize(db_conn_string())
    _db_session = Database()
    stock_repo = providers.Factory(StocksRepository, session=_db_session)
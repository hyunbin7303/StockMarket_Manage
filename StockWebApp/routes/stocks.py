from flask import request, jsonify, make_response, Response
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from db_session import database_instance
from models import Stock
from schemas import StockSchema, StockUpdateSchema,StockFinancialSchema
from psycopg.rows import dict_row
from werkzeug.exceptions import HTTPException
from repositories.stocksRepository import StocksRepository
from di.container import Container
from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject

stocks_bp = Blueprint("stocks", __name__, description="Operations on Stocks")

@stocks_bp.route('/stocks', methods=['GET'])
@stocks_bp.response(200, StockSchema(many=True))
@inject
def get_stocks(stock_repo: StocksRepository= Provide[Container.stock_repo]):
    result: list[Stock] = stock_repo.get_all()

    return result

@stocks_bp.route('/stocks/<int:stock_id>', methods=['GET'])
@inject
def get_stockbyId(stock_id: int, stock_repo: StocksRepository = Provide[Container.stock_repo]):
    result = stock_repo.get_by_id(stock_id)
    return result

@stocks_bp.route('/stocks/ticker/<string:ticker>')
@inject
def get_stock_by_ticker(ticker: str, stock_repo: StocksRepository = Provide[Container.stock_repo]):
    result = stock_repo.get_by_ticker(ticker)
    return result



@stocks_bp.route('/stocks', methods=['POST'])
@inject
def post(stock_repo: StocksRepository = Provide[Container.stock_repo]):
    try:
        check = stock_repo.get_by_ticker(request.json['ticker'])
        if check.len() > 0:
            abort(409, message="Already exist stock.")

        ticker =        request.json['ticker']
        company_name =  request.json['company_name']
        stock_desc =    request.json['stock_desc']
        stock_type =    request.json['stock_type']
        stock_sector =  request.json['stock_sector']
        stock_exchange = request.json['stock_exchange']
        new_stock = Stock(ticker, company_name, stock_desc, stock_type, stock_sector, stock_exchange)
        stock_repo.add(new_stock)
    except KeyError:
        abort(404, message= "Cannot insert the new stock")
    return Response({}, status=201)


@stocks_bp.response(200, StockSchema)
def delete(self, stock_id):
    try:
        # TODO : Find stock and delete
        #del stocks[stock_id]
        return {"message": "Stock has been removed"}
    except KeyError:
        abort(404, message= "Ticker cannot be found in stocks.")

# @stocks_bp.route("/stocks/<string:ticker>/financials")
#     def post(self, financial_data):
#         # financial_data = request.get_json()
#         # Check if ticker exists in the stock table.
#         # but do we need to do this if we are using the foreign key?
#         # Let's figure it out.
#         pass
def custom_error(message, status_code):
    return make_response(jsonify(message), status_code)

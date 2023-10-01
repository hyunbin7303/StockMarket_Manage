from flask import request, jsonify, make_response, Response
from flask_smorest import abort, Blueprint
from models import Stock
from schemas import InsertStockSchema
from psycopg.rows import dict_row
from repositories.stocksRepository import StocksRepository
from di.container import Container
from dependency_injector.wiring import Provide, inject

stocks_bp = Blueprint("stocks", __name__, description="Operations on Stocks")


@stocks_bp.route('/stocks', methods=['GET'])
# @stocks_bp.response(200, StockSchema(many=True))
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
@stocks_bp.arguments(InsertStockSchema)
@inject
def post(new_stock, stock_repo: StocksRepository = Provide[Container.stock_repo]):
    try:
        data = Stock(**new_stock)
        check = stock_repo.get_by_ticker(data.ticker)
        if check is not None:
            abort(409, message="Already exist stock.")

        stock_repo.add(data)
    except KeyError:
        abort(404, message= "Cannot insert the new stock")
    return Response({}, status=201)


@stocks_bp.route('/stocks/<int:stock_id>', methods=['DELETE'])
@inject
def delete(stock_id: int, stock_repo: StocksRepository = Provide[Container.stock_repo]):
    try:
        stock_repo.delete(stock_id)
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

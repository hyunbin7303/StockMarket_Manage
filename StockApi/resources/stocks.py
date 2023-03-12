import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from db import stocks

blueprint = Blueprint("stocks", __name__, description="Operations on Stocks")


@blueprint.route("/stocks/<string:ticker>")
class Stocks(MethodView):
    def get(self, ticker):
        try:
            return stocks[ticker]
        except KeyError:
            abort(404, message ="Ticker cannot be found in stocks.")

    def post(self):
        try:
            stock_data = request.get_json()
            stock_id = uuid.uuid4().hex
            new_stock = { **stock_data, "id": stock_id }
            
            for stock in stocks.values():
                if stock_data["ticker"] == stock["ticker"] or stock:
                    abort(400, message=f"Stock ticker already exist.")

            stocks[stock_id] = new_stock 
            return new_stock, 201
        except KeyError:
            abort(404, message="Tic")


    def put(self, ticker):
        stock_data = request.get_json()
        if "ticker" not in stock_data or "company_name" not in stock_data:
            abort(400, message="Bad Request. Ensure Symbol or company name are included in the json payload.")

        try:
            stock = stocks[ticker]
            stock |= stock_data
            return stock 
        except KeyError:
            abort(404, message="Stock not found")


    def delete(self, ticker):
        try:
            del stocks[ticker]
            return {"message": "Stock has been removed"}
        except KeyError:
            abort(404, message= "Ticker cannot be found in stocks.")
    def set(self, ticker):
        pass
    


@blueprint.route("/stocks")
class StocksList(MethodView):

    def get(self):
        return {"stocks" : list(stocks.values())}
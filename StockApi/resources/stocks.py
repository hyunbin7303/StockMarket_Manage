import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from db import stocks, stockFinancials
from schemas import StockSchema, StockUpdateSchema,StockFinancialSchema
blueprint = Blueprint("stocks", __name__, description="Operations on Stocks")


@blueprint.route("/stocks/ticker/<string:ticker>")
class StockTicker(MethodView):

    @blueprint.response(200, StockSchema)
    def get(self, ticker):
        try:
            pass # need to be updated after figuring out Stock endpoint practice. 
        except KeyError:
            abort(404, message="Ticker cannot be found.")

@blueprint.route("/stocks/<int:stock_id>")
class Stocks(MethodView):

    @blueprint.response(200, StockSchema)
    def get(self, stock_id):
        try:
            return stocks[stock_id]
        except KeyError:
            abort(404, message ="Ticker cannot be found in stocks.")


    @blueprint.arguments(StockUpdateSchema)
    @blueprint.response(200, StockSchema)
    def put(self, ticker):
        stock_data = request.get_json()

        try:
            stock = stocks[ticker]
            stock |= stock_data
            return stock 
        except KeyError:
            abort(404, message="Stock not found")


    @blueprint.response(200, StockSchema)
    def delete(self, stock_id):
        try:
            del stocks[stock_id]
            return {"message": "Stock has been removed"}
        except KeyError:
            abort(404, message= "Ticker cannot be found in stocks.")

@blueprint.route("/stocks")
class StocksList(MethodView):

    @blueprint.response(200, StockSchema(many=True)) 
    def get(self):
        return stocks.values()
    
    @blueprint.arguments(StockSchema)
    @blueprint.response(200,StockSchema)
    def post(self, stock_data):
        stock_data = request.get_json()
        for stock in stocks.values():
            if stock_data["ticker"] == stock["ticker"] or stock:
                abort(400, message=f"Stock ticker already exist.")

        stock_id = uuid.uuid4().hex
        new_stock = { **stock_data, "stock_id": stock_id }
        stocks[stock_id] = new_stock 
        return new_stock
    

@blueprint.route("/stocks/<string:ticker>/financials")
class StockFinancials(MethodView):

    def get(self):
        return stockFinancials
    
    @blueprint.arguments(StockFinancialSchema)
    def post(self, financial_data):
        financial_data = request.get_json()
        # Check if ticker exists in the stock table.
        # but do we need to do this if we are using the foreign key? 
        # Let's figure it out. 


        
        pass

    


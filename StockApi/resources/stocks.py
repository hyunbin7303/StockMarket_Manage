import uuid
import json
from utils import db_config
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from dbaccess import DbConnection
# from psycopg_pool import ConnectionPool
from schemas import StockSchema, StockUpdateSchema,StockFinancialSchema
blueprint = Blueprint("stocks", __name__, description="Operations on Stocks")


def my_function():
    with pool.connection() as conn:
        conn.execute(...)

    
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
            dbsetup = db_config()
            dbaccess = DbConnection(dbsetup['host'],dbsetup['username'], dbsetup['password'], dbsetup['port'], dbsetup['dbname'])
            result = dbaccess.select_rows("SELECT * FROM stocks where = stock_id = {}", stock_id)
            return result
        except KeyError:
            abort(404, message ="Ticker cannot be found in stocks.")


    @blueprint.arguments(StockUpdateSchema)
    @blueprint.response(200, StockSchema)
    def put(self, ticker):
        stock_data = request.get_json()

        try:
            # TODO : Find stock and update 
            stock = stocks[ticker]
            stock |= stock_data
            return stock 
        except KeyError:
            abort(404, message="Stock not found")


    @blueprint.response(200, StockSchema)
    def delete(self, stock_id):
        try:
            # TODO : Find stock and delete 
            del stocks[stock_id]
            return {"message": "Stock has been removed"}
        except KeyError:
            abort(404, message= "Ticker cannot be found in stocks.")

@blueprint.route("/stocks")
class StocksList(MethodView):

    @blueprint.response(200, StockSchema(many=True)) 
    def get(self):
        dbaccess = DbConnection("127.0.0.1", "postgres", "postgres", "5432", "FinanceDiary")
        result = dbaccess.select_rows("SELECT * FROM stocks;")
        return result
    
    @blueprint.arguments(StockSchema)
    @blueprint.response(200,StockSchema)
    def post(self, stock_data):


        dbsetup = db_config()
        dbaccess = DbConnection(dbsetup['host'],dbsetup['username'], dbsetup['password'], dbsetup['port'], dbsetup['dbname'])
        result = dbaccess.select_rows("SELECT * FROM stocks;")

        for stock in result:
            if stock_data["ticker"] == stock["ticker"] or stock:
                abort(400, message=f"Stock ticker already exist.")


        insert_query = 'insert', """INSERT INTO Stocks(ticker, company_name, stock_desc, stock_type, stock_sector,stock_exchange) VALUES (%s, %s, %s, %s, %s, %s);""",(stock_data['ticker'], stock_data['company_name'], stock_data['stock_desc'],stock_data['stock_type'],stock_data['stock_sector'],stock_data['stock_exchange'])
        dbaccess.command_query(insert_query)
        stock_data = request.get_json()
        # stock_id = uuid.uuid4().hex
        # new_stock = { **stock_data, "stock_id": stock_id }
        # stocks[stock_id] = new_stock 
        return 'success'
    

@blueprint.route("/stocks/<string:ticker>/financials")
class StockFinancials(MethodView):

    def get(self):
        return {}
    
    @blueprint.arguments(StockFinancialSchema)
    def post(self, financial_data):
        financial_data = request.get_json()
        # Check if ticker exists in the stock table.
        # but do we need to do this if we are using the foreign key? 
        # Let's figure it out. 

        pass

    

# Todo List. 
# How Python app is going to find Db access configuration one by one ? 
# Db Access as singleton which initially start when the app start? 
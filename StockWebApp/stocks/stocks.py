import uuid
from utils import db_config
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from dbaccess import DbConnection, Database
from db_session import database_instance
from schemas import StockSchema, StockUpdateSchema,StockFinancialSchema
from psycopg.rows import dict_row



stocks_bp = Blueprint("stocks", __name__, description="Operations on Stocks")

@stocks_bp.route('/<int:stock_id>', method=['GET'])
def get_stockbyId(stock_id: int):
    try:
        with database_instance.get_connection().connection() as conn:
            conn.execute("SELECT * FROM stocknews where ticker = {};", ticker)
    except KeyError:
        abort(404, message ="Ticker cannot be found in stocks.")

@stocks_bp.route('/ticker/<string:ticker>')
@stocks_bp.response(200, StockSchema)
def get_stock_by_ticker(ticker: str): 
    try:
        with database_instance.get_connection().connection() as conn:
            conn.execute("SELECT * FROM stocks where ticker = {};", ticker)
        pass # need to be updated after figuring out Stock endpoint practice.
    except KeyError:
        abort(404, message="Ticker cannot be found.")

@stocks_bp.route("/stocks/<int:stock_id>")
class Stocks(MethodView):

    @stocks_bp.response(200, StockSchema(many=True))
    def get(self, stock_id):
        query_str = 'SELECT * FROM stocks where stock_id =' + str(stock_id)
        try:

            dbsetup = db_config()
            dbaccess = DbConnection(dbsetup['host'],dbsetup['username'], dbsetup['password'], dbsetup['port'], dbsetup['dbname'])
            result = dbaccess.select_rows(query_str)
            return result
        except KeyError:
            abort(404, message ="Not Found.")


    @stocks_bp.arguments(StockUpdateSchema)
    @stocks_bp.response(200, StockSchema)
    def put(self, ticker):
        stock_data = request.get_json()

        try:
            # TODO : Find stock and update
            #stock = stocks[ticker]
            stock |= stock_data
            return stock
        except KeyError:
            abort(404, message="Stock not found")


    @stocks_bp.response(200, StockSchema)
    def delete(self, stock_id):
        try:
            # TODO : Find stock and delete
            #del stocks[stock_id]
            return {"message": "Stock has been removed"}
        except KeyError:
            abort(404, message= "Ticker cannot be found in stocks.")

@stocks_bp.route("/stocks", methods=['GET', 'POST'])
class StocksList(MethodView):

    @stocks_bp.response(200, StockSchema(many=True))
    def get(self):

        try:
            with database_instance.get_connection() as conn:
                cur = conn.cursor(row_factory=dict_row)
                result = cur.execute("SELECT * FROM stocks;").fetchall()
        except KeyError:
            abort(404, message="Ticker cannot be found.")
            
        return result

    @stocks_bp.arguments(StockSchema)
    @stocks_bp.response(200,StockSchema)
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

@stocks_bp.route("/stocks/<string:ticker>/financials")
class StockFinancials(MethodView):

    def get(self):
        return {}

    @stocks_bp.arguments(StockFinancialSchema)
    def post(self, financial_data):
        financial_data = request.get_json()
        # Check if ticker exists in the stock table.
        # but do we need to do this if we are using the foreign key?
        # Let's figure it out.

        pass


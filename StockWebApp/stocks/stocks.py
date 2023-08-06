import uuid
from flask import request, jsonify, make_response, Response
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from dbaccess import DbConnection, Database
from db_session import database_instance
from models import Stock
from schemas import StockSchema, StockUpdateSchema,StockFinancialSchema
from psycopg.rows import dict_row
from werkzeug.exceptions import HTTPException



stocks_bp = Blueprint("stocks", __name__, description="Operations on Stocks")

@stocks_bp.route('/stocks', methods=['GET'])
@stocks_bp.response(200, StockSchema(many=True))
def get_stocks(): 

    try:
        with database_instance.get_connection() as conn:
            cur = conn.cursor(row_factory=dict_row)
            result = cur.execute("SELECT * FROM stocks;").fetchall()

    except KeyError:
        abort(404, message="Ticker cannot be found.")
    finally:
        cur.close()
        database_instance.return_connection(conn)

    return result


@stocks_bp.route('/stocks/<int:stock_id>', methods=['GET'])
def get_stockbyId(stock_id: int):
    try:
        with database_instance.get_connection() as conn:
            cur = conn.cursor()
            cur.execute("""select * from stocks where stock_id = %(stock_id)s """, {"stock_id": stock_id})
            rows = cur.fetchall()

    except KeyError:
        abort(404, message ="Ticker cannot be found in stocks.")

    finally:
        cur.close()
        database_instance.return_connection(conn)    

    return rows

@stocks_bp.route('/ticker/<string:ticker>')
@stocks_bp.response(200, StockSchema)
def get_stock_by_ticker(ticker: str): 
    try:
        with database_instance.get_connection() as conn:
            conn.execute("SELECT * FROM stocks where ticker = %{ticker}s;", {ticker: ticker})
            cur = conn.cursor()
        pass # need to be updated after figuring out Stock endpoint practice.
    except KeyError:
        abort(404, message="Ticker cannot be found.")
    finally:
        cur.close()
        database_instance.return_connection(conn)    


@stocks_bp.route('/stocks', methods=['POST'])
def post():
    try: 
        ticker =        request.json['ticker']
        company_name =  request.json['company_name']
        stock_desc =    request.json['stock_desc']
        stock_type =    request.json['stock_type']
        stock_sector =  request.json['stock_sector']
        stock_exchange = request.json['stock_exchange']
        # new_stock = Stock(ticker, company_name, stock_desc, stock_type, stock_sector, stock_exchange)
    except KeyError:
        abort(404, message= "Cannot insert the new stock")
    
    try:
        with database_instance.get_connection() as conn:
            cur = conn.cursor()
            cur.execute("""select * from stocks where ticker = %(ticker)s """, {"ticker": ticker})
            rows = cur.fetchone()
            if rows:
                raise KeyError("Already Exist Tickers = ", ticker)

            cur.execute("""INSERT INTO stocks(ticker, company_name, stock_desc, stock_type, stock_sector,stock_exchange) VALUES (%(ticker)s, %(company_name)s, %(stock_desc)s, %(stock_type)s, %(stock_sector)s, %(stock_exchange)s)""", 
                        {"ticker": ticker, "company_name": company_name, "stock_desc":stock_desc, "stock_type": stock_type, "stock_sector": stock_sector, "stock_exchange":stock_exchange})

            conn.commit()
            cur.close()

    except KeyError as err:
        return Response(err.args, status=403)
    except ValueError as err:
        return Response(err.args, status =404)

    finally:
        database_instance.return_connection(conn)

    data={
        "StatusCode": 200, 
        "Subject": "Successful"
    }
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

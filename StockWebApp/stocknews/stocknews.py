import uuid
import string
from flask import request, jsonify, make_response, Response
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from schemas import StockNewsSchema
from db_session import database_instance
from psycopg.rows import dict_row
from stocks.stocksRepository import StocksRepository

stocknews_bp = Blueprint("stocknews", __name__, description="Operations on StockNews")

@stocknews_bp.route('/stocknews/<string:stocknews_id>')
@stocknews_bp.response(201, StockNewsSchema)
def get_by_stocknewsId(stocknews_id: string):
    try:
        with database_instance.get_connection() as conn:
            conn.execute("SELECT * FROM stocknews where stocknews_id = {};", stocknews_id)
    except KeyError:
        abort(404, message ="Ticker cannot be found in stocks.")

@stocknews_bp.route('/stocknews', methods=['GET'])
@stocknews_bp.response(201, StockNewsSchema(many=True))
def get_all():
    # @blueprint.response(200, StockNewsSchema(many=True)) 
    try:
        with database_instance.get_connection() as conn:
            cur = conn.cursor(row_factory=dict_row)
            result = cur.execute("SELECT * FROM stocknews;").fetchall()
    except KeyError:
        abort(404, message = "Unexpected things happened")
    finally:
        cur.close()
        database_instance.return_connection(conn)
            
    return result


@stocknews_bp.route('/<string:stocknews_id>')
def put_stocknews(stocknews_id):
    
    news_data = request.get_json()
    if "ticker" not in news_data or "title" not in news_data:
        abort(400, message="Bad request. Ensure ticker and title are included in the json payload.")
    try:
        # news = stockNews[stocknews_id]
        news |= news_data
    except KeyError:
        abort(404, message="news not found")
         
@stocknews_bp.route('/stocknews/<int:stock_id>', methods=['POST'])
# @stocknews_bp.response(201, StockNewsSchema(many=True))
def post(stock_id: int):
    stock_repo = StocksRepository()
    stock = stock_repo.get_by_id(stock_id)
    if stock is None:
        abort(404, message="Stock Id is not exist in stocks.")

    title =  request.json['title']
    cause =    request.json['cause']
    impact_on_stock = request.json['impact_on_stock']
    price_before = request.json['price_before']
    try:
        with database_instance.get_connection() as conn:
            cur = conn.cursor()
            cur.execute("""select * from stocknews where title = %(title)s """, {"title": title})
            rows = cur.fetchone()
            if rows:
                raise KeyError("Already Exist title = ", title)
            cur.execute("""INSERT INTO stocknews(stock_id, title, price_before, cause, impact_on_stock) VALUES (%(stock_id)s, %(title)s, %(price_before)s, %(cause)s, %(impact_on_stock)s)""", 
                        {"stock_id": stock_id, "title": title, "price_before": price_before, "cause": cause, "impact_on_stock": impact_on_stock})

            conn.commit()
            cur.close()

    except KeyError as err:
        return Response(err.args, status=403)
    except ValueError as err:
        return Response(err.args, status =404)

    finally:
        database_instance.return_connection(conn)

    return Response({}, status=201)

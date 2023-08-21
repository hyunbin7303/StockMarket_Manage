import uuid
import string
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from schemas import StockNewsSchema
from db_session import database_instance
from psycopg.rows import dict_row

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


@stocknews_bp.route('/stocknews')

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
         
@stocknews_bp.route('/stocksnews', methods=['POST'])
def post():
    try: 
        news_id = request.json['news_id']
        title =  request.json['title']
#        price_before =    request.json['price_before']
        cause =    request.json['cause']
        impact_on_stock = request.json['impact_on_stock']
        price_before = request.json['price_before']
        # new_stock = Stock(ticker, company_name, stock_desc, stock_type, stock_sector, stock_exchange)
    except KeyError:
        abort(404, message= "Cannot insert the new stock news")
    
    try:
        with database_instance.get_connection() as conn:
            cur = conn.cursor()
            cur.execute("""select * from stocksnews where title = %(title)s """, {"title": title})
            rows = cur.fetchone()
            if rows:
                raise KeyError("Already Exist title = ", title)

            cur.execute("""INSERT INTO stocksnews(news_id, title, price_before, cause, impact_on_stock) VALUES (%(news_id)s, %(title)s, %(price_before)s, %(cause)s, %(impact_on_stock)s)""", 
                        {"news_id": news_id, "title": title, "price_before": price_before, "cause": cause, "impact_on_stock": impact_on_stock})

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

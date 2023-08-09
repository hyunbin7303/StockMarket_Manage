import uuid
import string
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from schemas import StockNewsSchema
from db_session import database_instance
from psycopg.rows import dict_row

stocknews_bp = Blueprint("stockNews", __name__, description="Operations on StockNews")

@stocknews_bp.route('/stocknews/<string:stocknews_id>')
@stocknews_bp.response(201, StockNewsSchema)
def get_by_stocknewsId(stocknews_id: string):
    try:
        with database_instance.get_connection() as conn:
            conn.execute("SELECT * FROM stocknews where stocknews_id = {};", stocknews_id)
    except KeyError:
        abort(404, message ="Ticker cannot be found in stocks.")

@stocknews_bp.route('/stocknews')
@stocknews_bp.response(201, StockNewsSchema)
def get_all():
    # @blueprint.response(200, StockNewsSchema(many=True)) 
    try:
        with database_instance.get_connection() as conn:
            cur = conn.cursor(row_factory=dict_row)
            result = cur.execute("SELECT * FROM stocknews;").fetchall()
    except KeyError:
        abort(404, message = "Unexpected things happened")
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


# How this stock can impact existing 
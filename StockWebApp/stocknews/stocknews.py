import uuid
import string
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from dbaccess import DbConnection
from schemas import StockNewsSchema
from db_session import database_instance

stocknews_bp = Blueprint("stockNews", __name__, description="Operations on StockNews")

@stocknews_bp.route('/<string:stocknews_id>')
@stocknews_bp.response(201, StockNewsSchema)
def get_by_stocknewsId(stocknews_id: string):
    try:
        with database_instance.get_connection().connection() as conn:
            conn.execute("SELECT * FROM stocknews where stocknews_id = {};", stocknews_id)
    except KeyError:
        abort(404, message ="Ticker cannot be found in stocks.")

@stocknews_bp.route('/')
@stocknews_bp.response(201, StockNewsSchema)
def get_all():
    # @blueprint.response(200, StockNewsSchema(many=True)) 
    try:
        with database_instance.get_connection().connection() as conn:
            conn.execute("SELECT * FROM stocksnews", ticker)
    except KeyError:
        abort(404, message = "Unexpected things happened")
    # return stockNews.values()

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


# @stocknews_bp.route('/<string:stocknews_id>', method=['DELETE'])
# def delete_stocknews(stocknews_id: str):
#     try:
#         del stockNews[stocknews_id]
#         return {"message": "Stock has been removed"}
#     except KeyError:
#         abort(404, message= "Ticker cannot be found in stocks.")

# @stocknews_bp.route("/", method=['POST'])
# @stocknews_bp.arguments(StockNewsSchema)
# @stocknews_bp.response(201, StockNewsSchema)
# def create_stocknews(self, news_data)-> None:
#     news_data = request.get_json()

#     # if news_data["stock_id"] not in stocks:
#     #     return abort(404, message="Stock not found, so stock news cannot be stored.")
        
#     news_id = uuid.uuid4().hex
#     news = {**news_data, "id": news_id}
#         # stockNews[news_id] = news  
#     return news

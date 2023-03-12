import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from db import stockNews, stocks
from schemas import StockNewsSchema, StockNewsUpdateSchema

blueprint = Blueprint("stockNews", __name__, description="Operations on StockNews")


@blueprint.route("/stocknews/<string:stocknews_id>")
class StockNews(MethodView):


    def get(self, stocknews_id):
        try:
            return stockNews[stocknews_id]
        except KeyError:
            abort(404, message ="Ticker cannot be found in stocks.")


    def put(self, stocknews_id):
        news_data = request.get_json()
        if "ticker" not in news_data or "title" not in news_data:
            abort(400, message="Bad request. Ensure ticker and title are included in the json payload.")

        try:
            news = stockNews[stocknews_id]
            news |= news_data
        except KeyError:
            abort(404, message="news not found")


    def delete(self, stocknews_id):
        try:
            del stockNews[stocknews_id]
            return {"message": "Stock has been removed"}
        except KeyError:
            abort(404, message= "Ticker cannot be found in stocks.")
 


@blueprint.route("/stocknews")
class StockNewsList(MethodView):

    def get(self):
        return {"stocknews" : list(stockNews.values())}

    @blueprint.arguments(StockNewsSchema)
    def post(self, news_data):
        news_data = request.get_json()

        if news_data["stock_id"] not in stocks:
            return abort(404, message="Stock not found, so stock news cannot be stored.")
        
        news_id = uuid.uuid4().hex
        news = {**news_data, "id": news_id}
        stockNews[news_id] = news  
        return news

import string
from models.stocknews import StockNews
from flask import request, jsonify, make_response, Response
from flask_smorest import abort, Blueprint
from schemas import StockNewsSchema
from repositories.stocknews_repository import StocknewsRepository
from repositories.stocksRepository import StocksRepository
from di.container import Container
from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject
from datetime import date

stocknews_bp = Blueprint("stocknews", __name__,url_prefix='/stocknews', description="Operations on StockNews")

@stocknews_bp.route('/', methods=['GET'])
@stocknews_bp.response(201, StockNewsSchema(many=True))
@inject
def get_all(repo: StocknewsRepository= Provide[Container.stocknews_repo]):
    result = repo.get_all()
    return result

@stocknews_bp.route('/<string:stocknews_id>')
@stocknews_bp.response(201, StockNewsSchema)
@inject
def get_by_stocknewsId(stocknews_id: string, repo: StocknewsRepository= Provide[Container.stocknews_repo]):
    result = repo.get_by_id(stocknews_id)
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

@stocknews_bp.route('/', methods=['POST'])
@inject
def post(repo: StocknewsRepository= Provide[Container.stocknews_repo], stock_repo: StocksRepository= Provide[Container.stock_repo]):
    stock_id = request.json['stock_id']
    stock = stock_repo.get_by_id(stock_id)
    if stock is None:
        abort(404, message="Stock Id is not exist in stocks.")

    news = StockNews(stock_id= stock_id,
                     title= request.json['title'],
                     news_desc= request.json['news_desc'],
                     cause = request.json['cause'],
                     impact_on_stock=request.json['impact_on_stock'],
                     price_before=request.json['price_before'],
                     price_after=request.json['price_after'],
                     news_date = request.json['news_date'],
                     record_date = date.today())
    repo.add(news)
    return Response({}, status=201)

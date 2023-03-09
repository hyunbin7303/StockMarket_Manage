import uuid
from flask import Flask,request
from flask_smorest import abort
from db import stockInfo, stocks


app = Flask(__name__) 






# [
#     {
#         "ticker" : "MSFT",
#         "company_name" : "Microsoft",
#         "items": [
#             {
#                 "name": "Chair",
#                 "price": 20
#             }
#         ]
#     }
# ] 

# @ is python decorator 
@app.get("/stocks")
def get_stocks():
    return { "stocks": list(stocks.values())}

@app.get("/stocks/<string:ticker>")
def get_stocks_by_ticker(ticker):
    try:
        for stock in stocks:
            if stock["ticker"] == ticker:
                return stock
    except KeyError:
         return abort(404, message="Stock not found")
 
@app.get("/stocks/ById/<string:stock_id>")
def get_stocks_by_id(stock_id):
    try:
        return stocks[stock_id]
    except KeyError:
         return abort(404, message="Stock not found")

# @app.get("/stocks/<string:ticker>/item")
# def get_stocks_by_ticker(ticker):
#     for stock in stocks:
#         if stock["ticker"] == ticker:
#             return {"items" : stock["items"]} 
#     return {"message": "Stock cannot be found"}, 404


@app.post("/stocks")
def create_new_stock():
    stock_data = request.get_json()
    stock_id = uuid.uuid4().hex
    new_stock = { **stock_data, "id": stock_id }
    stocks[stock_id] = new_stock 
    return new_stock, 201
    
@app.post("/stockinfo")
def create_info():
    info_data = request.get_json()
    if info_data["stock_id"] not in stocks:
         return abort(404, message="Stock not found")
     
    info_id = uuid.uuid4().hex
    info = {**info_data, "id": info_id}
    stockInfo[info_id] = info  

    return info, 201

@app.get("/stockinfos")
def get_all_infos():
    return {"infos" : list(stockInfo.values())}


@app.get("/stockinfo/<string:stockinfo_id>")
def get_stockinfo_byId(stockinfo_id):
    try:
        return stockInfo[stockinfo_id]
    except KeyError:
        return abort(404, message="Stock not found")
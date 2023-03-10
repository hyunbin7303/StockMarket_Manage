import uuid
from flask import Flask,request
from flask_smorest import abort
from db import stockNews, stocks

app = Flask(__name__) 

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
 
@app.get("/stocks/ById/<int:stock_id>")
def get_stocks_by_id(stock_id):
    try:
        return stocks[stock_id]
    except KeyError:
         return abort(404, message="Stock not found")

@app.post("/stocks")
def create_new_stock():
    stock_data = request.get_json()
    stock_id = uuid.uuid4().hex
    new_stock = { **stock_data, "id": stock_id }
    
    for stock in stocks.values():
        if stock_data["ticker"] == stock["ticker"]:
            abort(400, message=f"Stock ticker already exist.")

    stocks[stock_id] = new_stock 
    return new_stock, 201
    
@app.put("/stocks/<int:stock_id>")
def update_stock(stock_id):
    stock_data = request.get_json()
    if "symbol" not in stock_data or "company_name" not in stock_data:
        abort(400, message="Bad Request. Ensure Symbol or company name are included in the json payload.")

    try:
        stock = stocks[stock_id]
        stock |= stock_data
        return stock 
    except KeyError:
        abort(404, message="Stock not found")

@app.get("/stocknews")
def get_all_news():
    return {"news" : list(stockNews.values())}

@app.get("/stocknews/<string:stocknews_id>")
def get_stockNews_byId(stockinfo_id):
    try:
        return stockNews[stockinfo_id]
    except KeyError:
        return abort(404, message="Stock not found")

@app.post("/stocknews")
def create_stock_news():
    news_data = request.get_json()

    if "ticker" not in news_data or "title" not in news_data:
        abort(400, message= "Bad request. Ensure 'ticker' and 'title' are included in the Json payload. ")
    

    # for new in stockNews.values():
        # if news_data[""]

    if news_data["stock_id"] not in stocks:
        return abort(404, message="Stock not found")
     
    news_id = uuid.uuid4().hex
    news = {**news_data, "id": news_id}
    stockNews[news_id] = news  

    return news, 201

@app.post("/stocknews/<string:news_id>")
def update_stocknews(news_id):
    news_data = request.get_json()
    if "ticker" not in news_data or "title" not in news_data:
        abort(400, message="Bad request. Ensure ticker and title are included in the json payload.")

    try:
        news = stockNews[news_id]
        news |= news_data
    except KeyError:
        abort(404, message="news not found")

@app.delete("/stocknews/<string:news_id>")
def delete_stocknews(news_id):
    try:
        del stockNews[news_id]
        return {"message" : "news deleted"}
    except KeyError:
        abort(404, message="news not found")

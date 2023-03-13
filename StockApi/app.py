import os
from flask import Flask
from flask_smorest import Api
from dbaccess import DbConnection

# import DbConnection
import models

from resources.stocks import blueprint as StockBlueprint
from resources.stocknews import blueprint as StockNewsBlueprint

query_create_stock_table = '''CREATE TABLE IF NOT EXISTS Stocks
(
    stock_id SERIAL PRIMARY KEY,
    ticker character varying(50) COLLATE pg_catalog."default" NOT NULL,
    company_name character varying(100) COLLATE pg_catalog."default" NOT NULL,
    stock_desc character varying(500) COLLATE pg_catalog."default",
	stock_type varchar(50),
	stock_sector varchar(50),
    stock_exchange character varying(100) COLLATE pg_catalog."default",
    listing_date date
);
ALTER TABLE IF EXISTS public.stocks OWNER to postgres;'''
query_create_indicator_table = '''CREATE TABLE IF NOT EXISTS Indicators
(
    indicator_id SERIAL PRIMARY KEY,
    "Index" character varying(40) COLLATE pg_catalog."default" NOT NULL,
    "Name" character varying(100) COLLATE pg_catalog."default" NOT NULL,
    "Desc" character varying(450) COLLATE pg_catalog."default",
    "Country" character varying(50) COLLATE pg_catalog."default"
)'''
query_create_StockNews_table = '''CREATE TABLE IF NOT EXISTS StockNews
(
 	news_id uuid DEFAULT uuid_generate_v4(),
	stock_id INT,
	title VARCHAR(150), 
	news_desc VARCHAR(255),
	Cause VARCHAR(50),	
	Impact_On_Stock VARCHAR(50), -- Such as BreakOut, FlagPole, Pennant, Flag, Pole etc..BullishFlag, BearishFlag,. 
	Price_Before bigint,
	Price_After bigint, 
	News_Date date,
	Record_Date date, 
	PRIMARY KEY(news_id), 
	CONSTRAINT fk_stock_id FOREIGN KEY(stock_id) REFERENCES stocks(stock_id)
)
TABLESPACE pg_default;'''

def create_app(db_url = None):


    app = Flask(__name__)


    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    # db.init_app(app)
    api = Api(app)
    # with app.app_context():
    #     db.create_all()
    dbaccess = DbConnection("127.0.0.1", "postgres", "postgres", "5432", "FinanceDiary")
    dbaccess.db_create_init_tables(query_create_stock_table)
    dbaccess.db_create_init_tables(query_create_indicator_table)
    dbaccess.db_create_init_tables(query_create_StockNews_table)

    api.register_blueprint(StockNewsBlueprint)
    api.register_blueprint(StockBlueprint)


    return app
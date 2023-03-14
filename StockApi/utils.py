from configparser import ConfigParser
from dbaccess import DbConnection
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


def db_config():
    config = ConfigParser()
    config.read("config.ini")
    dbsetup = config["DATABASE"]
    return dbsetup

def db_conn_string():
    dbinfo = db_config()
    dbstr = f"User ID={dbinfo['username']};Password{dbinfo['password']};Port={dbinfo['port']};Host={dbinfo['host']} Database={dbinfo['dbname']}"
    return dbstr

def create_init_db():
    dbsetup = db_config()
    dbaccess = DbConnection(dbsetup['host'],dbsetup['username'], dbsetup['password'], dbsetup['port'], dbsetup['dbname'])
    dbaccess.db_create_init_tables(query_create_stock_table)
    dbaccess.db_create_init_tables(query_create_indicator_table)
    dbaccess.db_create_init_tables(query_create_StockNews_table)
    # db access, create table for Daily
    # db access, Create table for financial 
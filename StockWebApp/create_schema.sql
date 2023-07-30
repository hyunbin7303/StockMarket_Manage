CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
DROP TABLE IF EXISTS StockNews;
DROP TABLE IF EXISTS Stocks;
DROP TABLE IF EXISTS StockFinancials;
-- DROP TABLE IF EXISTS StockDaily;
DROP TABLE IF EXISTS Indicators;
DROP TABLE IF EXISTS IndicatorData;

CREATE TABLE IF NOT EXISTS Stocks
(
    stock_id serial PRIMARY KEY,
    ticker character varying(50) COLLATE pg_catalog."default" NOT NULL,
    company_name character varying(100) COLLATE pg_catalog."default" NOT NULL,
    stock_desc character varying(500) COLLATE pg_catalog."default",
    stock_type character varying(50) COLLATE pg_catalog."default",
    stock_sector character varying(50) COLLATE pg_catalog."default",
    stock_exchange character varying(100) COLLATE pg_catalog."default",
    listing_date date
);


CREATE TABLE IF NOT EXISTS StockNews
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
TABLESPACE pg_default;

CREATE TABLE IF NOT EXISTS StockFinancials
(
    financial_id UUID NOT NULL, -- This field seems it needs to be UUID field.
    "equity " bigint,
    total_revenue bigint,
    gross_profit bigint,
    liability bigint,
    "net_income" bigint,
    "EBITDA" bigint,
	"quarter" varchar(20), 
	
    record_time date,
    CONSTRAINT "StockFinancials_pkey" PRIMARY KEY (financial_id)
);
	
CREATE TABLE IF NOT EXISTS Indicators
(
    "indicator_id" serial PRIMARY KEY,
    "Index" character varying(40) COLLATE pg_catalog."default" NOT NULL,
    "Name" character varying(100) COLLATE pg_catalog."default" NOT NULL,
    "Desc" character varying(450) COLLATE pg_catalog."default",
    "Country" character varying(50) COLLATE pg_catalog."default"
);
	
CREATE TABLE IF NOT EXISTS IndicatorData
(
	"id" UUID NOT NULL,
	"indicator_id" INT,
	"value" bigint,
	"announced_date" date, 
	"recorded_date" date,
	"date_source" varchar(50)
);

INSERT INTO public.indicators ("Index", "Name", "Desc", "Country") VALUES ('CPI', 'Consumer Price Index', 'A consumer price index is a price index, the price of a weighted average market basket of consumer goods and services purchased by households. ', 'US');
INSERT INTO public.indicators ("Index", "Name", "Desc", "Country") VALUES ('CPI', 'Consumer Price Index', 'A consumer price index is a price index, the price of a weighted average market basket of consumer goods and services purchased by households. ', 'CANADA');
INSERT INTO public.indicators ("Index", "Name", "Desc", "Country") VALUES ('CPI', 'Consumer Price Index', 'A consumer price index is a price index, the price of a weighted average market basket of consumer goods and services purchased by households. ', 'SOUTH KOREA');
INSERT INTO public.indicators ("Index", "Name", "Desc", "Country") VALUES ('CPI', 'Consumer Price Index', 'A consumer price index is a price index, the price of a weighted average market basket of consumer goods and services purchased by households. ', 'JAPAN');
INSERT INTO public.indicators ("Index", "Name", "Desc", "Country") VALUES ('CPI', 'Consumer Price Index', 'A consumer price index is a price index, the price of a weighted average market basket of consumer goods and services purchased by households. ', 'CHINA');
INSERT INTO public.indicators ("Index", "Name", "Desc", "Country") VALUES ('CPI', 'Consumer Price Index', 'A consumer price index is a price index, the price of a weighted average market basket of consumer goods and services purchased by households. ', 'UNITED KINGDOM');
INSERT INTO public.indicators ("Index", "Name", "Desc", "Country") VALUES ('PMI', 'Purchasing Managers Index', 'The Purchasing Managers Index (PMI) is an index of the prevailing direction of economic trends in the manufacturing and service sectors. ', 'US');
INSERT INTO public.indicators ("Index", "Name", "Desc", "Country") VALUES ('PMI', 'Purchasing Managers Index', 'The Purchasing Managers Index (PMI) is an index of the prevailing direction of economic trends in the manufacturing and service sectors. ', 'CHINA');
INSERT INTO public.indicators ("Index", "Name", "Desc", "Country") VALUES ('SOX', 'Philadelphia Semiconductor Index', 'The PHLX Semiconductor Sector IndexSM (SOXSM) is a modified market capitalization-weighted index composed of companies primarily involved in the design, distribution, manufacture, and sale of semiconductors.', 'US');

INSERT INTO Stocks(ticker, company_name, "stock_desc", "stock_type", stock_exchange) VALUES ('MSFT', 'Microsoft', 'Microsoft Organization', 'stock','NASDAQ');

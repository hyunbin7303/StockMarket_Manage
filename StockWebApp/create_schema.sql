-- Table: public.Stocks
-- figure out dif between chracter varying vs VCHAR.
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";



DROP TABLE IF EXISTS Stocks;
-- Inserting data in Stock table 
INSERT INTO Stocks(ticker, company_name, description, stock_type, stock_exchange) VALUES ('MSFT', 'Microsoft', 'Microsoft Organization', 'stock','NASDAQ');





DROP TABLE IF EXISTS StockNews;
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

DROP TABLE IF EXISTS StockFinancials;
CREATE TABLE IF NOT EXISTS StockFinancials
(
    financial_id UUID NOT NULL, -- This field seems it needs to be UUID field.
    "equity " bigint,
    total_revenue bigint,
    gross_profit bigint,
    liability bigint,
    net_income bigint,
    "EBITDA" bigint,
	quarter varchar(20), 
	
    record_time date,
    CONSTRAINT "StockFinancials_pkey" PRIMARY KEY (financial_id)
)




DROP TABLE IF EXISTS Indicators;
CREATE TABLE IF NOT EXISTS public.indicators
(
    "indicator_id" integer NOT NULL DEFAULT nextval('indicators_indicator_id_seq'::regclass),
    "Index" character varying(40) COLLATE pg_catalog."default" NOT NULL,
    "Name" character varying(100) COLLATE pg_catalog."default" NOT NULL,
    "Desc" character varying(450) COLLATE pg_catalog."default",
    "Country" character varying(50) COLLATE pg_catalog."default",
    CONSTRAINT indicators_pkey PRIMARY KEY (indicator_id)
);

TABLESPACE pg_default;

INSERT INTO public.indicators VALUES (1, 'CPI', 'Consumer Price Index', 'A consumer price index is a price index, the price of a weighted average market basket of consumer goods and services purchased by households. ', 'US');
INSERT INTO public.indicators VALUES (2, 'CPI', 'Consumer Price Index', 'A consumer price index is a price index, the price of a weighted average market basket of consumer goods and services purchased by households. ', 'CANADA');
INSERT INTO public.indicators VALUES (3, 'CPI', 'Consumer Price Index', 'A consumer price index is a price index, the price of a weighted average market basket of consumer goods and services purchased by households. ', 'SOUTH KOREA');
INSERT INTO public.indicators VALUES (4, 'CPI', 'Consumer Price Index', 'A consumer price index is a price index, the price of a weighted average market basket of consumer goods and services purchased by households. ', 'JAPAN');
INSERT INTO public.indicators VALUES (5, 'CPI', 'Consumer Price Index', 'A consumer price index is a price index, the price of a weighted average market basket of consumer goods and services purchased by households. ', 'CHINA');
INSERT INTO public.indicators VALUES (6, 'CPI', 'Consumer Price Index', 'A consumer price index is a price index, the price of a weighted average market basket of consumer goods and services purchased by households. ', 'UNITED KINGDOM');

-- PMI? 
-- It consists of a diffusion index that summarizes whether market conditions, as viewed by purchasing managers, are expanding, staying the same, or contracting. 
-- The purpose of the PMI is to provide information about current and future business conditions to company decision makers, analysts, and investors.
INSERT INTO public.indicators VALUES (7, 'PMI', 'Purchasing Managers Index', 'The Purchasing Managers Index (PMI) is an index of the prevailing direction of economic trends in the manufacturing and service sectors. ', 'US');
INSERT INTO public.indicators VALUES (8, 'PMI', 'Purchasing Managers Index', 'The Purchasing Managers Index (PMI) is an index of the prevailing direction of economic trends in the manufacturing and service sectors. ', 'CHINA');
INSERT INTO public.indicators VALUES (9, 'SOX', 'Philadelphia Semiconductor Index', 'The PHLX Semiconductor Sector IndexSM (SOXSM) is a modified market capitalization-weighted index composed of companies primarily involved in the design, distribution, manufacture, and sale of semiconductors.', 'US');


DROP TABLE IF EXISTS IndicatorData;
CREATE TABLE IF NOT EXISTS IndicatorData
(
	id UUID NOT NULL,
	indicator_id INT,
	"value" bigint,
	"announced_date" date, 
	"recorded_date" date,
	date_source varchar(50)
)

	
select * from Indicators
select * from stocks
select * from StockNews
SELECT * FROM StockFinancials

-- 4 Key Indicators that move the markets.
-- Employment - The most important indicator of the health of the economy.
-- the unemployment rate tracks the number of workers who are currently out of jobs.
-- The nonfarm payrolls report tracks the number of jobs that have been added or eliminated in the economy overall.

-- Inflaion 
-- The mandate of the Federal Reserve is to promote economy growth and price stability in the economy.
-- Price stability is measured as the rate of change in inflation, so market participants eagerly monitor monthly inflation reports to determine the
-- future course of the Federal Reserve's monetary policy.
-- There are many indicators of inflation, but perhaps the most closely watched is the CPI. the CPI measures the change in the price of ordinary good that most people
-- spend money on, such as clothing and medical services. 



CREATE TABLE PINK_FLOYD (
	id uuid DEFAULT uuid_generate_v4 (),
	album_name VARCHAR NOT NULL,
	release_date DATE NOT NULL,
	PRIMARY KEY (id)
);
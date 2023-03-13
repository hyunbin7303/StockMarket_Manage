-- Table: public.Stocks
-- figure out dif between chracter varying vs VCHAR.
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";



DROP TABLE IF EXISTS Stocks;
-- Inserting data in Stock table 
INSERT INTO Stocks(ticker, company_name, description, stock_type, stock_exchange) VALUES ('MSFT', 'Microsoft', 'Microsoft Organization', 'stock','NASDAQ');
DROP TABLE IF EXISTS Indicators;

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
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



stocks = {}
stockNews = {
    1: {
        "ticker" : "MSFT",
        "Title" : "MSFT info",
        "Description" : ""
    },
    2: {
        "ticker":"TSLA",
        "Title": "TSLA NEWS",
        "Description" : "Why it goes down..."
    }
} 
stockFinancials = {}


def db_access():
    pass

def sql_query():
    pass

def create_tables():
    pass

def create_sample_data():
    pass
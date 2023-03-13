from db import db


class StockModel(db.Model):
    __tablename__ = "stock"
    stock_id = db.Column(db.Integer, primary_key = True)
    ticker = db.Column(db.String(100), unique= True, nullable = False)
    company_name = db.Column(db.String(100), unique=True, nullable= False)
    stock_desc = db.Column(db.String(255), nullable = False),
    stock_type = db.Column(db.String(50), nullable = False),
    stock_sector = db.Column(db.String(50), nullable = False),
    stock_exchange = db.Column(db.String(100), nullable = False),
    stocknews = db.relationship("StockNewsModel", back_populates = "stock", lazy="dynamic")

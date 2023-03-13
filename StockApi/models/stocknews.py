


# class StockNewsModel(db.Model):
#     __tablename__ = "stocknews" 

#     news_id = db.Column(db.String, primary_key = True)
#     stock_id = db.Column(db.Integer, db.ForeignKey("stock.id"), unique=False, nullable = False)
#     title = db.Column(db.String, unique=False, nullable= False)
#     news_desc = db.Column(db.String(255))
#     stock = db.relationship("StockModel", back_populates="stocknews")
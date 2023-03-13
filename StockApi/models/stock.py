class Stock:

    def __init__(self, ticker, company_name, desc, type,sector,exchange):
        self.ticker = ticker
        self.company_name = company_name
        self.stock_desc = desc
        self.stock_type = type
        self.stock_sector = sector
        self.stock_exchange = exchange
# class StockModel(dbaccess.Model):
#     __tablename__ = "stock"
#     stock_id = dbaccess.Column(dbaccess.Integer, primary_key = True)
#     ticker = dbaccess.Column(dbaccess.String(100), unique= True, nullable = False)
#     company_name = dbaccess.Column(dbaccess.String(100), unique=True, nullable= False)
#     stock_desc = dbaccess.Column(dbaccess.String(255), nullable = False),
#     stock_type = dbaccess.Column(dbaccess.String(50), nullable = False),
#     stock_sector = dbaccess.Column(dbaccess.String(50), nullable = False),
#     stock_exchange = dbaccess.Column(dbaccess.String(100), nullable = False),
#     stocknews = dbaccess.relationship("StockNewsModel", back_populates = "stock", lazy="dynamic")

from marshmallow import Schema, fields

class BasicStockSchema(Schema):
    stock_id = fields.Int(dump_only=True)
    ticker = fields.Str(required=True)
    company_name = fields.Str(required=True)
    stock_desc = fields.Str()
    stock_type = fields.Str()
    stock_exchange = fields.Str()

class StockUpdateSchema(Schema):
    stock_id = fields.Str()
    company_name = fields.Str()
    description = fields.Str()
    stock_type = fields.Str()

class BasicStockNewsSchema(Schema):
    news_id = fields.Str(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str()
    cause = fields.Str()
    impact_on_stock = fields.Str()
    price_before = fields.Int()
    

class StockNewsUpdateSchema(Schema):
    news_id = fields.Str()
    title = fields.Str(required=True)
    description = fields.Str()

class StockSchema(BasicStockSchema):
    stocknews = fields.List(fields.Nested(BasicStockNewsSchema()), dump_only=True)
class StockNewsSchema(BasicStockNewsSchema):
    stock_id = fields.Int(required=True)
    stock = fields.Nested(lambda: BasicStockSchema(), dump_only= True)
class StockFinancialSchema(Schema):
    financial_id = fields.Int(dump_only=True)
    stock_id = fields.Int(required=True)
    equity = fields.Int()
    gross_profit = fields.Int() 
    liability = fields.Int()
    net_income = fields.Int()
    EBITDA  = fields.Int()
    quarter = fields.Str()

     
class IndicatorsSchema(Schema):
    indicator_id = fields.Int(required=True)
    index = fields.Str()
    Name = fields.Str()
    Desc = fields.Str()
    Country = fields.Str()

class IndicatordataSchema(Schema):
    indicator_id = fields.Int(dump_only=True)
    value = fields.Int()
    announced_date = fields.Str()
    recorded_date = fields.Str()
    date_source = fields.Str()
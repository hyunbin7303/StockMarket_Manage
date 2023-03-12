from marshmallow import Schema, fields


class StockSchema(Schema):
    stock_id = fields.Str(dump_only=True) 
    ticker = fields.Str(required=True)
    company_name = fields.Str(required=True)

class StockUpdateSchema(Schema):
    stock_id = fields.Str()

class StockNewsSchema(Schema):
    news_id = fields.Str(dump_only=True)
    stock_id = fields.Int(required=True)
    title = fields.Str(required=True)
    description = fields.Str()
    cause = fields.Str()
    impact_on_stock = fields.Str()
    price_before = fields.Int()

class StockNewsUpdateSchema(Schema):
    news_id = fields.Str()
    title = fields.Str(required=True)
    description = fields.Str()


     

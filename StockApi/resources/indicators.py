import uuid
from utils import db_config
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from dbaccess import DbConnection, Database
from db_session import database_instance
from schemas import IndicatorsSchema
from psycopg.rows import dict_row

blueprint = Blueprint("indicators", __name__, description="Operations on Indicators")


@blueprint.route("/indicators")
class Indicators(MethodView):


    @blueprint.response(200, IndicatorsSchema(many=True))
    def get(self):

        try:
            with database_instance.get_connection() as conn:
                cur = conn.cursor(row_factory=dict_row)
                result = cur.execute("SELECT * FROM indicators;").fetchall()
        except KeyError:
            abort(404, message="No indicators.")
            
        return result

@blueprint.route("/indicators/<int:indicator_id>")
class IndicatorsById(MethodView):


    @blueprint.response(200, IndicatorsSchema(many=True))
    def get(self, indicator_id):
        query_str = 'SELECT * FROM indicators where indicator_id =' + str(indicator_id)
        try:

            dbsetup = db_config()
            dbaccess = DbConnection(dbsetup['host'],dbsetup['username'], dbsetup['password'], dbsetup['port'], dbsetup['dbname'])
            result = dbaccess.select_rows(query_str)
            return result
        except KeyError:
            abort(404, message ="Not Found.")


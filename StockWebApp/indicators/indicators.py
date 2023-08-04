import uuid
from utils import db_config
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from dbaccess import DbConnection, Database
from db_session import database_instance
from schemas import IndicatorsSchema
from psycopg.rows import dict_row

indicators_bp = Blueprint("indicators", __name__, description="Operations on Indicators")


@indicators_bp.route("/indicators")
class Indicators(MethodView):


    @indicators_bp.response(200, IndicatorsSchema(many=True))
    def get(self):

        try:
            with database_instance.get_connection() as conn:
                cur = conn.cursor(row_factory=dict_row)
                result = cur.execute("SELECT * FROM indicators;").fetchall()


        except KeyError:
            abort(404, message="No indicators.")
            # database_instance.close_all_connections()
        finally:
            cur.close()
            database_instance.return_connection(conn)
        return result


@indicators_bp.route('/indicators/<int:indicator_id>', methods=['GET'])
def get_stockbyId(indicator_id: int):
    try:
        with database_instance.get_connection() as conn:
            cur = conn.cursor()
            query_str = 'SELECT * FROM indicators where indicator_id =' + str(indicator_id)
            cur.execute(query_str)
            rows = cur.fetchall()

    except KeyError:
        abort(404, message ="Ticker cannot be found in stocks.")

    finally:
        cur.close()
        database_instance.return_connection(conn)    

    return rows
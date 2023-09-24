from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from db_session import database_instance
from schemas import IndicatorsSchema
from psycopg.rows import dict_row

indicators_bp = Blueprint("indicators", __name__, description="Operations on Indicators")

@indicators_bp.route('/indicators', methods=['GET'])
@indicators_bp.response(200, IndicatorsSchema(many=True))
def get_indicators():
    try:
        with database_instance.get_connection() as conn:
            cur = conn.cursor(row_factory=dict_row)
            result = cur.execute("SELECT * FROM indicators;").fetchall()

    except KeyError:
        abort(404, message="")
    finally:
        cur.close()
        database_instance.return_connection(conn)

    return result

@indicators_bp.route('/indicators/<int:indicator_id>', methods=['GET'])
def get_indicator_byId(indicator_id: int):
    try:
        with database_instance.get_connection() as conn:
            cur = conn.cursor()
            cur.execute("""select * from indicators where indicator_id = %(indicator_id)s """, {"indicator_id": indicator_id})
            rows = cur.fetchall()

    except KeyError:
        abort(404, message ="Ticker cannot be found in stocks.")

    finally:
        cur.close()
        database_instance.return_connection(conn)    

    return rows

@indicators_bp.route('/indicators', methods=['POST'])
def insert_indicator():
    try:
        pass
    except KeyError:
        abort(404, message = "")
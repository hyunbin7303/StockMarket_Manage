from flask_smorest import abort
from psycopg.rows import dict_row
from dbaccess import Database
from models import stock, stocknews

class IndicatorsRepository:
    _db_session:Database

    def __init__(self, session: Database) -> None:
        self._db_session = session

    def get_all(self):
        try:
            with self._db_session.get_connection() as conn:
                cur = conn.cursor(row_factory=dict_row)
                result = cur.execute("SELECT * FROM indicators;").fetchall()

        except KeyError:
            abort(404, message="Ticker cannot be found.")
        finally:
            cur.close()
            self._db_session.return_connection(conn)

        return result if result is not None else None



    def get_by_id(self, indicator_id: int):
        try:
            with self._db_session.get_connection() as conn:
                cur = conn.cursor()
                cur.execute("""select * from indicators where indicator_id = %(indicator_id)s """, {"indicator_id": indicator_id})
                rows = cur.fetchall()
        except KeyError:
            abort(404, message ="Ticker cannot be found in stocks.")

        finally:
            cur.close()
            self._db_session.return_connection(conn)

        return rows

    def get_by_stock_id(self, ticker: str):
        try:
            with self._db_session.get_connection() as conn:
                cur = conn.cursor()
                result =cur.execute("""select * from stocks where ticker = %(ticker)s """, {"ticker": ticker}).fetchall()
        except KeyError:
            abort(404, message="Ticker cannot be found.")
        finally:
            cur.close()
            self._db_session.return_connection(conn)

        return result if result is not None else None


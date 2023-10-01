from flask_smorest import abort
from psycopg.rows import dict_row
from dbaccess import Database
from models import stock, indicatordata

class IndicatordataRepository:
    _db_session:Database

    def __init__(self, session: Database) -> None:
        self._db_session = session

    def get_all(self):
        try:
            with self._db_session.get_connection() as conn:
                cur = conn.cursor(row_factory=dict_row)
                result = cur.execute("SELECT * FROM indicatordata;").fetchall()

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
                cur.execute("""select * from indicatordata where indicator_id = %(indicator_id)s """, {"indicator_id": indicator_id})
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


    def add(self, indicatordata: indicatordata) -> None:
        try:

            with self._db_session.get_connection() as conn:
                cur = conn.cursor()
                cur.execute("""INSERT INTO indicatordata(indicator_id, value, announced_date, recorded_date, date_source) VALUES (%(value)s, %(value)s, %(announced_date)s, %(recorded_date)s, %(date_source)s)""",
                            {"indicator_id":indicatordata.indicator_id, "value": indicatordata.value, "announced_date": indicatordata.announced_date, "recorded_date":indicatordata.recorded_date, "date_source": indicatordata.date_source})
                conn.commit()
                cur.close()

        except ValueError as err:
            abort(404, message="Cannot add indicatordata Exception :" + err)
        finally:
            self._db_session.return_connection(conn)
from flask_smorest import abort
from psycopg.rows import dict_row
from dbaccess import Database
from models import stock, stocknews

class StocknewsRepository:
    _db_session:Database

    def __init__(self, session: Database) -> None:
        self._db_session = session

    def get_all(self):
        try:
            with self._db_session.get_connection() as conn:
                cur = conn.cursor(row_factory=dict_row)
                result = cur.execute("SELECT * FROM stocknews;").fetchall()

        except KeyError:
            abort(404, message="Ticker cannot be found.")
        finally:
            cur.close()
            self._db_session.return_connection(conn)

        return result if result is not None else None



    def get_by_id(self, stocknews_id: int):
        try:
            with self._db_session.get_connection() as conn:
                cur = conn.cursor()
                row =cur.execute("""select * from stocknews where news_id = %(news_id)s """, {"news_id": stocknews_id}).fetchone()

        except KeyError:
            abort(404, message ="Ticker cannot be found in stocks.")

        finally:
            cur.close()
            self._db_session.return_connection(conn)

        return row

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


    def add(self, stocknews: stocknews):
        try:
            with self._db_session.get_connection() as conn:
                cur = conn.cursor()
                cur.execute("""select * from stocknews where title = %(title)s """, {"title": stocknews.title})
                rows = cur.fetchone()
                if rows:
                    raise KeyError("Already Exist title = ", stocknews.title)

                cur.execute("""INSERT INTO stocknews(stock_id, title, price_before, cause, impact_on_stock) VALUES (%(stock_id)s, %(title)s, %(price_before)s, %(cause)s, %(impact_on_stock)s)""",
                            {"stock_id": stocknews.stock_id, "title": stocknews.title, "price_before": stocknews.price_before, "cause": stocknews.cause, "impact_on_stock": stocknews.impact_on_stock})

                conn.commit()
                cur.close()

        except KeyError as err:
            abort(403, message="Key Error Exception : " + err.args)

        except ValueError as err:
            abort(404, message="xception : " + err.args)

        finally:
            self._db_session.return_connection(conn)


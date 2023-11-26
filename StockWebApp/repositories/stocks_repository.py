# from db_session import database_instance
from flask_smorest import abort
from psycopg.rows import dict_row
from dbaccess import Database
from models import Stock

class StocksRepository:
    _db_session:Database

    def __init__(self, session: Database) -> None:
        self._db_session = session

    def get_all(self):
        try:
            with self._db_session.get_connection() as conn:
                cur = conn.cursor(row_factory=dict_row)
                result = cur.execute("SELECT * FROM stocks;").fetchall()

        except KeyError:
            abort(404, message="Ticker cannot be found.")
        finally:
            cur.close()
            self._db_session.return_connection(conn)

        return result if result is not None else None



    def get_by_id(self, stock_id: int) -> Stock | None:
        try:
            with self._db_session.get_connection() as conn:
                cur = conn.cursor()
                rows =cur.execute("""select * from stocks where id = %(id)s """, {"id": stock_id}).fetchall()

        except KeyError:
            abort(404, message ="Ticker cannot be found in stocks.")

        finally:
            cur.close()
            self._db_session.return_connection(conn)

        return rows

    def get_by_ticker(self, ticker: str)-> Stock | None:
        try:
            with self._db_session.get_connection() as conn:
                cur = conn.cursor()
                result =cur.execute("""select * from stocks where ticker = %(ticker)s """, {"ticker": ticker}).fetchone()
        except KeyError:
            abort(404, message="Ticker cannot be found.")
        finally:
            cur.close()
            self._db_session.return_connection(conn)

        return result if result is not None else None


    def add(self, stock: Stock) -> None:
        try:

            with self._db_session.get_connection() as conn:
                cur = conn.cursor()
                cur.execute("""INSERT INTO stocks(ticker, company_name, stock_desc, stock_type, stock_sector,stock_exchange) VALUES (%(ticker)s, %(company_name)s, %(stock_desc)s, %(stock_type)s, %(stock_sector)s, %(stock_exchange)s)""",
                            {"ticker": stock.ticker, "company_name": stock.company_name, "stock_desc":stock.stock_desc, "stock_type": stock.stock_type, "stock_sector": stock.stock_sector, "stock_exchange":stock.stock_exchange})
                conn.commit()
                cur.close()

        except ValueError as err:
            abort(404, message="Cannot add stock. Exception :" + err)
        finally:
            self._db_session.return_connection(conn)


    def delete(self, stock_id: int) -> None:
        try:
            with self._db_session.get_connection() as conn:
                cur = conn.cursor()
                cur.execute("""DELETE from stocks where id = %(id)s """, {"id": stock_id})
                conn.commit()
                cur.close()

        except ValueError as err:
            abort(404, message="cannot remove stock. Exception : " + err)

        finally:
            self._db_session.return_connection(conn)


    def update(self, stock: Stock):
        pass
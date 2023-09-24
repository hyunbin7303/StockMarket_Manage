from db_session import database_instance
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
            database_instance.return_connection(conn)

        return result if result is not None else None



    def get_by_id(self, stock_id: int) -> Stock | None:
        try:
            with database_instance.get_connection() as conn:
                cur = conn.cursor()
                rows =cur.execute("""select * from stocks where stock_id = %(stock_id)s """, {"stock_id": stock_id}).fetchall()

        except KeyError:
            abort(404, message ="Ticker cannot be found in stocks.")

        finally:
            cur.close()
            database_instance.return_connection(conn)

        return rows

    def get_by_ticker(self, ticker: str)-> list[Stock] | None:
        try:
            with database_instance.get_connection() as conn:
                cur = conn.cursor()
                result =cur.execute("""select * from stocks where ticker = %(ticker)s """, {"ticker": ticker}).fetchall()
        except KeyError:
            abort(404, message="Ticker cannot be found.")
        finally:
            cur.close()
            database_instance.return_connection(conn)

        return result if result is not None else None


    def add(self, stock: Stock):
        try:

            with database_instance.get_connection() as conn:
                cur = conn.cursor()
                cur.execute("""INSERT INTO stocks(ticker, company_name, stock_desc, stock_type, stock_sector,stock_exchange) VALUES (%(ticker)s, %(company_name)s, %(stock_desc)s, %(stock_type)s, %(stock_sector)s, %(stock_exchange)s)""",
                            {"ticker": stock.ticker, "company_name": stock.company_name, "stock_desc":stock.stock_desc, "stock_type": stock.stock_type, "stock_sector": stock.stock_sector, "stock_exchange":stock.stock_exchange})
                conn.commit()
                cur.close()

        except ValueError as err:
            pass
            # return Response(err.args, status =404)
        finally:
            database_instance.return_connection(conn)

    def delete(self, stock_id: int):
        pass

    def update(self, stock: Stock):
        pass
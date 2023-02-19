import psycopg2
from psycopg2 import Error

# example from https://github.com/masroore/pg_simple/blob/master/pg_simple/pg_simple.py
class DbConnection:
    def __init__(self,Host,Username,Pwd,Port,Name):
        self.host = Host
        self.username = Username
        self.password = Pwd
        self.port = Port
        self.dbname = Name
        self.conn = self.get_conn()

    def get_conn(self): 
        try:
            conn = psycopg2.connect(dbname=self.dbname,user=self.username,host=self.host, port=self.port, password=self.password)
        except psycopg2.OperationalError as err:
            err_msg = 'DB Connection Error - Error: {}'.format(err)
            print(err_msg)
            return False
        return conn
    def execute(self,sql_raw, params, qry_type):
        try:
            cur.execute(sql_raw, params)
            if qry_type == 'sel_single':
                results = cur.fetchone()
            elif qry_type == 'sel_multi':
                results = cur.fetchall()
            elif qry_type == 'insert':
                results = cur.fetchone()
                conn.commit()
            elif qry_type == 'update':
                results = cur.fetchone()
                conn.commit()
            else:
                raise Exception('Invalid query type defined.')

        except psycopg2.ProgrammingError as err:
            print('Database error via psycopg2.  %s', err)
            results = False
        except psycopg2.IntegrityError as err:
            print('PostgreSQL integrity error via psycopg2.  %s', err)
            results = False
        finally:
            conn.close()

        return results

    def db_create_init_tables(self):
        print("Create tables if not exist.")

    def select_rows(self, query):
        # self.connect()
        with self.conn.cursor() as cur:
            cur.execute(query)
            records = cur.fetchall()
        cur.close()
        return records


    def dbaccess_test(self):
        try:
            connection = psycopg2.connect(dbname="FinanceDiary",user="postgres",host="127.0.0.1", port="5432", password="Cc7594435!")
            cursor = connection.cursor()
            print(connection.get_dsn_parameters(), "\n")
            # Executing a SQL query
            cursor.execute("SELECT version();")
            # Fetch result
            record = cursor.fetchone()
            print("You are connected to - ", record, "\n")

        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
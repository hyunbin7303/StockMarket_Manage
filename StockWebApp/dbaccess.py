import psycopg
from psycopg import Error
from psycopg_pool import ConnectionPool
from psycopg.rows import dict_row

class Database:
    __pool = None
    __connStr = ''
    @classmethod
    def initialize(cls, connStr):
        __connStr = connStr
        cls.__pool = ConnectionPool(__connStr)

    @classmethod
    def get_connection(cls):
        if cls.__pool.check():
            cls.pool.putconn(cls.pool.getconn())
        return cls.__pool.getconn()
        


    @classmethod
    def return_connection(cls, connection):
        return cls.__pool.putconn(connection)

    @classmethod
    def close_all_connections(cls):
        Database.__pool.closeall()


class DbConnection:
# # example from https://github.com/masroore/pg_simple/blob/master/pg_simple/pg_simple.py
    def __init__(self,Host,Username,Pwd,Port,Name):
        self.host = Host
        self.username = Username
        self.password = Pwd
        self.port = Port
        self.dbname = Name
        self.conn = self.get_conn()
        
    def get_conn(self, connStr = None): 
        try:                
            
            conn = psycopg.connect(dbname=self.dbname,user=self.username,host=self.host, port=self.port, password=self.password)
        except psycopg.OperationalError as err:
            err_msg = 'DB Connection Error - Error: {}'.format(err)
            print(err_msg)
            return False
        return conn
    
    def execute(self,sql_raw, params, qry_type):
        try:
            cur = self.conn.cursor()
            cur.execute(sql_raw, params)
            if qry_type == 'sel_single':
                results = cur.fetchone()
            elif qry_type == 'sel_multi':
                results = cur.fetchall()
            elif qry_type == 'insert':
                results = cur.fetchone()
                self.conn.commit()
            elif qry_type == 'update':
                results = cur.fetchone()
                self.conn.commit()
            else:
                raise Exception('Invalid query type defined.')

        except psycopg.ProgrammingError as err:
            print('Database error via psycopg2.  %s', err)
            results = False
        except psycopg.IntegrityError as err:
            print('PostgreSQL integrity error via psycopg2.  %s', err)
            results = False
        finally:
            self.conn.close()

        return results

    def db_create_init_tables(self, query):
        conn = self.get_conn()
        try:
            cur = conn.cursor()
            create_script = query
            cur.execute(create_script)
            conn.commit()
            conn.close()
        except Exception as err:
            print(err)
        finally:
            conn.close()


    def select_rows(self, query): #  sel_multi
        with self.conn.cursor(row_factory=dict_row) as cur:
            cur.execute(query)
            records = cur.fetchall()
        cur.close()
        return records

    def select_specific(self, query):
        pass


    def command_query(self, query_type, query):
        try:
            cur = self.conn.cursor()
            if query_type == 'insert':
                results = cur.fetchone()
                self.conn.commit()
            elif query_type == 'update':
                results = cur.fetchone()
                self.conn.commit()

        except psycopg.ProgrammingError as err:
            print('Database error via psycopg2.  %s', err)
            result = False
        except psycopg.IntegrityError() as err:
            print('PostgreSQL integrity error via psycopg2.  %s', err)
            result = False
        
        return result

def create_conn_pool(connStr):
    pool = ConnectionPool(connStr)






# def sql_query():
#     pass

# def create_tables():
#     pass

# def create_sample_data():
#     pass
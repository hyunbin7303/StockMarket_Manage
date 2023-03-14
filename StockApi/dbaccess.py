import psycopg2
from psycopg2 import Error
from psycopg2.extras import RealDictCursor




class DbConnection:
# # example from https://github.com/masroore/pg_simple/blob/master/pg_simple/pg_simple.py
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

        except psycopg2.ProgrammingError as err:
            print('Database error via psycopg2.  %s', err)
            results = False
        except psycopg2.IntegrityError as err:
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
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
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

        except psycopg2.ProgrammingError as err:
            print('Database error via psycopg2.  %s', err)
            result = False
        except psycopg2.IntegrityError() as err:
            print('PostgreSQL integrity error via psycopg2.  %s', err)
            result = False
        
        return result






# def sql_query():
#     pass

# def create_tables():
#     pass

# def create_sample_data():
#     pass
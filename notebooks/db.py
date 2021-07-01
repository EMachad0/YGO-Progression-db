import os
import psycopg2

conn = None

def connect(verbose=False):
    global conn
    if conn is not None:
        return conn
    try:
        if verbose:
            print('DB Connecting')
        conn = psycopg2.connect(os.environ['DATABASE_URL'])
        if verbose:
            print('DB Connected')
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        raise (Exception('Error while connecting to DB: ' + str(error)))

def make_query(query, data):
    try:
        con = connect(verbose=True)
        cur = con.cursor()
        cur.execute(query, data)
        con.commit()
        cur.close()
    except (Exception, psycopg2.Error) as err:
        print(err)
        raise err

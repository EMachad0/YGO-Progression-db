import os
import psycopg2

def connect(verbose=False):
    try:
        if verbose:
            print('DB Connecting')
        con = psycopg2.connect(os.environ['DATABASE_URL'])
        if verbose:
            print('DB Connected')
        return con
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        raise (Exception('Error while connecting to DB: ' + str(error)))

def make_query(query, data):
    con = None
    cur = None
    try:
        con = connect()
        cur = con.cursor()
        cur.execute(query, data)
        con.commit()
    except (Exception, psycopg2.Error) as err:
        print(err)
        raise err
    finally:
        if con:
            cur.close()
            con.close()
import psycopg2
import yaml
import os
from dotenv import load_dotenv
load_dotenv()

def connect():
    return psycopg2.connect(dbname=    os.environ['DB_DATABASE'],
                            user=    os.environ['DB_USER'],
                            password=    os.environ['DB_PASSWORD'],
                            host=    os.environ['DB_IP'],
                            port=    os.environ['DB_PORT']
)


def exec_sql_file(path):
    full_path = os.path.join(os.path.dirname(__file__), f'../../{path}')
    conn = connect()
    cur = conn.cursor()
    with open(full_path, 'r') as file:
        cur.execute(file.read())
    conn.commit()
    conn.close()

def exec_get_one(sql, args={}):
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql, args)
    one = cur.fetchone()
    conn.close()
    return one

def exec_get_all(sql, args={}):
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql, args)
    # https://www.psycopg.org/docs/cursor.html#cursor.fetchall

    list_of_tuples = cur.fetchall()
    conn.close()
    return list_of_tuples

def exec_commit(sql, args={}):
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql, args)
    result = cur.rowcount
    conn.commit()
    conn.close()
    return result

def exec_commit_return(sql, args={}):
    conn = connect()
    cur = conn.cursor()
    cur.execute(sql, args)
    one = cur.fetchone()
    conn.commit()
    conn.close()
    return one
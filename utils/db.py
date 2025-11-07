from utils import config
import psycopg2
import psycopg2.extras
from psycopg2 import pool

#connect to database using database url
#This connection has been replaced with the connection_pool below. Keeping it here for now case it's needed again.
# connection = psycopg2.connect(config.DB_URL)

#connection pool 
connection_pool = psycopg2.pool.SimpleConnectionPool(
    minconn = 1,
    maxconn = 10,
    dsn = config.DB_URL
)


#re-usable database query function
def query(sql, params=None, fetchone=False):
    # Run an SQL query and return results as dictionaries
    connection = connection_pool.getconn()
    with connection:
        with connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            cursor.execute(sql, params or ())
            if fetchone:
                return cursor.fetchone()
            else:
                return cursor.fetchall()

#re-usable database INSERT, UPDATE, DELETE function          
def execute(sql, params=None):
    connection = connection_pool.getconn()
    # Run an SQL query that doesn't return rows
    with connection:
        with connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            cursor.execute(sql, params or ())
            return cursor.rowcount
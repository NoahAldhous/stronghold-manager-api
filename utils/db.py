from utils import config
import psycopg2
import psycopg2.extras

#connect to database using database url
connection = psycopg2.connect(config.DB_URL)

#re-usable database query function
def query(sql, params=None, fetchone=False):
    # Run an SQL query and return results as dictionaries
    with connection:
        with connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            cursor.execute(sql, params or ())
            if fetchone:
                return cursor.fetchone()
            else:
                return cursor.fetchall()

#re-usable database INSERT, UPDATE, DELETE function          
def execute(sql, params=None):
    # Run an SQL query that doesn't return rows
    with connection:
        with connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            cursor.execute(sql, params or ())
            return cursor.rowcount
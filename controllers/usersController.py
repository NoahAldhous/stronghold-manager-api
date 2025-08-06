from models.Users import GET_ALL_USERS
from config import connection


def get_all_users():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(GET_ALL_USERS)
            rows = cursor.fetchall()
    return {"message": "success!", "data": rows}, 200
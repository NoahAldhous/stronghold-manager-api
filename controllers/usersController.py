from models.Users import GET_ALL_USERS, CREATE_USERS_TABLE, INSERT_USER_RETURN_ID, GET_USER_BY_ID
from config import connection
from flask import request
from datetime import date
import psycopg2.extras

# get all users
def get_all_users():
    with connection:
        with connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            cursor.execute(GET_ALL_USERS)
            rows = cursor.fetchall()
    return {"message": f"success!", "data": rows}, 200

# create new user 
def create_user():
    data = request.get_json()
    name = data["name"]
    email = data["email"]
    password = data["password"]
    account_created = date.today()
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_USERS_TABLE)
            cursor.execute(INSERT_USER_RETURN_ID, (name, email, password, account_created,))
            user_id = cursor.fetchone()[0]
    return {"id": user_id, "message": f"User {name} created with email {email} and password {password} on {account_created}"}, 201

# get user by id
def get_user_by_id(user_id):
    with connection:
        with connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            cursor.execute(GET_USER_BY_ID, (user_id,))
            response = cursor.fetchone()
        return {"message": f"Success!", "data": response}, 200
from models.Users import GET_ALL_USERS, CREATE_USERS_TABLE, INSERT_USER_RETURN_ID, GET_USER_BY_ID, UPDATE_USER_NAME_BY_ID, UPDATE_USER_PASSWORD_BY_ID, DELETE_USER_BY_ID
from utils.db import query, connection, execute
from flask import request
from datetime import date

# GET ALL USERS
def get_all_users():
    users = query(GET_ALL_USERS, fetchone=False)
    
    if users:
        return {"message": "Success!", "data": users}, 200
    else:
        return {"message": "data not found"}, 404

# CREATE NEW USER
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

# GET USER BY ID
def get_user_by_id(user_id):
    user = query(GET_USER_BY_ID, (user_id,), fetchone=True)
    
    if user:
        return {"message": "Success!", "data": user}, 200
    else: 
        return {"message": "User not found"}, 404
    
# UPDATE PASSWORD BY ID
def update_user_password_by_id(user_id):
    data = request.get_json()
    newPassword = data["password"]
    res = execute(UPDATE_USER_PASSWORD_BY_ID, (newPassword, user_id,))
    
    if res:
        return {"message": "Password updated in " + str(res) + " user"}, 200
    else: return {"message": "User not found"}, 404

# UPDATE USER NAME BY ID    
def update_user_name_by_id(user_id):
    data = request.get_json()
    newUsername = data["username"]
    res = execute(UPDATE_USER_NAME_BY_ID, (newUsername, user_id))
    
    if res:
        return {"message": "Username updated in " + str(res) + " user"}, 200
    else: return {"message": "User not found"}, 404
    
# DELETE USER BY ID
def delete_user_by_id(user_id):
    res = execute(DELETE_USER_BY_ID, (user_id,))
    
    if res:
        return {"message": "User deleted", "number of rows deleted": res}, 200
    else: return {"message": "User not found"}, 404
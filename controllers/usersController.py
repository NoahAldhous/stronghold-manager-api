from models.Users import GET_ALL_USERS, CREATE_USERS_TABLE, INSERT_USER, GET_USER_BY_ID, GET_USER_BY_EMAIL, UPDATE_USER_NAME_BY_ID, UPDATE_USER_ROLE_BY_ID, UPDATE_USER_PASSWORD_BY_ID, DELETE_USER_BY_ID, DELETE_USERS_TABLE
from utils.db import query, execute
from flask_jwt_extended import create_access_token, get_jwt
from utils.auth import hash_password, verify_password
from flask import request

# CREATE USERS TABLE
def create_users_table():
    res = execute(CREATE_USERS_TABLE)
    
    if res:
        return {"message" : "Table created"}, 200
    else: 
        return {"message" : "Oops, an error occured"}, 404

# GET ALL USERS
def get_all_users():
    users = query(GET_ALL_USERS, fetchone=False)
    
    if users:
        return {"message": "Success!", "data": users}, 200
    else:
        return {"message": "data not found"}, 404

# REGISTER NEW USER
def register_user():
    data = request.get_json()
    name = data["name"]
    email = data["email"]
    password_hash = hash_password(data["password"])
    
    #check if user email is unique
    existing = query(GET_USER_BY_EMAIL, (email,), fetchone=True)
    if existing:
        return {"message" : "Email already in use"}, 409
    
    user = query(INSERT_USER, (name, email, password_hash))
    
    if user:
        token = create_access_token(identity=str(user["id"]), additional_claims={"role": user["role"], "user_name": user["user_name"]})
        return {"access_token": token}, 201
    else:
        return {"message": "Error, could not create user"}, 400

# LOGIN USER
def login_user():
    data = request.get_json()
    email = data["email"]
    password = data["password"]
    
    # look up the user
    user= query(GET_USER_BY_EMAIL, (email,), fetchone=True)
    if not user or not verify_password(password, user["password_hash"]):
        return {"message" : "invalid credentials, login failed"}, 401
    
    # add claims like 'role'
    token = create_access_token(identity=str(user["id"]), additional_claims={"role": user["role"], "user_name": user["user_name"]})
    return {"access_token" : token}, 200

# WHO AM I
def whoami():
    claims = get_jwt()
    user_id = claims["sub"]
    role = claims.get("role")
    user_name = claims.get("user_name")
    return {"user_id" : user_id, "role" : role, "user_name" : user_name}

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
    newPasswordHash = hash_password(data["password"])
    res = execute(UPDATE_USER_PASSWORD_BY_ID, (newPasswordHash, user_id,))
    
    if res:
        return {"message": "Password updated in " + str(res) + " user"}, 200
    else: return {"message": "User not found"}, 404

# UPDATE USER ROLE BY ID
def update_user_permission_by_id(user_id):
    data = request.get_json()
    newRole = data["role"]
    res = execute(UPDATE_USER_ROLE_BY_ID, (newRole, user_id))
    
    if res:
        return {"message": "Permission updated in " + str(res) + " user"}, 200
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
    
#DELETE USERS TABLE
def delete_users_table():
    res = execute(DELETE_USERS_TABLE)
    
    if res: 
        return {"message" : "table deleted"}, 200
    else:
        return {"message" : "table not found"}, 404
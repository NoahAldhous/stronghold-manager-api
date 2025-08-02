import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from datetime import date

CREATE_USERS_TABLE = (
    "CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, user_name TEXT, email TEXT, user_password TEXT, account_created DATE);"
)

CREATE_STRONGHOLD_CONSTRUCTION_LEVELS_TABLE = ()

CREATE_STRONGHOLD_SIZE_LEVELS_TABLE = ()

CREATE_CLASS_STRONGHOLD_ACTIONS_TABLE = ()

CREATE_CLASS_DEMESNE_EFFECTS_TABLE = ()

CREATE_CLASS_FEATURE_IMPROVEMENTS_TABLE = ()

CREATE_STRONGHOLD_TOUGHNESS_LEVELS_TABLE = ()

CREATE_STRONGHOLD_CLASSES_TABLE = ()

CREATE_STRONGHOLD_SUB-TYPES_TABLE = ()

CREATE_STRONGHOLD_TYPES_TABLE = ()

CREATE_STRONGHOLD_TYPE_FEATURES_TABLE = ()

CREATE_STRONGHOLDS_TABLE = (
    "CREATE TABLE IF NOT EXISTS strongholds (id SERIAL PRIMARY KEY, FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE, stronghold_name TEXT, level_id INTEGER, FOREIGN KEY(stronghold_type_id) REFERENCES stronghold_types(id), FOREIGN KEY(stronghold_sub-type_id) REFERENCES stronghold_sub-types(id), FOREIGN KEY(stronghold_class_id) REFERENCES stronghold_class(id),  created_at TIMESTAMP, )"
)



INSERT_USER_RETURN_ID = "INSERT INTO users (user_name, email, user_password, account_created) VALUES (%s, %s, %s, %s) RETURNING id;"

INSERT_STRONGHOLD = "INSERT INTO strongholds (stronghold_name, created_at) VALUES (%s, %s);"

GET_ALL_USERS = "SELECT * FROM users;"

#Parse .env file and load all variables found within
load_dotenv()

app = Flask(__name__)
#This CANNOT be called url, it takes the env from smartpantry for some reason.
dburl = os.getenv("STRONGHOLD_DATABASE_URL")
connection = psycopg2.connect(dburl)

#create new user endpoint
@app.post("/users/")
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

#get all users endpoint
@app.route("/users/getall/", methods=['GET'])
def get_all_users():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(GET_ALL_USERS)
            rows = cursor.fetchall()
    return {"message": "success!", "data": rows}, 200
            
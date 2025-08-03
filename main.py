import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from datetime import date

CREATE_USERS_TABLE = (
    "CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, user_name TEXT, email TEXT, user_password TEXT, account_created DATE);"
)

CREATE_STRONGHOLD_CONSTRUCTION_LEVELS_TABLE = (
    "CREATE TABLE IF NOT EXISTS stronghold_construction_levels (id SERIAL PRIMARY KEY, stronghold_level INTEGER, FOREIGN KEY(stronghold_type_id) REFERENCES stronghold_types(id), cost_to_build INTEGER, time_to_build INTEGER, fortification_morale_bonus INTEGER);"
)

CREATE_STRONGHOLD_SIZE_LEVELS_TABLE = (
    "CREATE TABLE IF NOT EXISTS stronghold_size_levels (id SERIAL PRIMARY KEY, stronghold_level INTEGER, FOREIGN KEY(stronghold_type_id) REFERENCES stronghold_types(id), stronghold_size INTEGER);"
)

CREATE_CLASS_STRONGHOLD_ACTIONS_TABLE = (
    "CREATE TABLE IF NOT EXISTS class_stronghold_actions (id SERIAL PRIMARY KEY, FOREIGN KEY(stronghold_class_id) REFERENCES stronghold_classes(id), action_description TEXT);"
)

CREATE_CLASS_DEMESNE_EFFECTS_TABLE = (
    "CREATE TABLE IF NOT EXISTS class_demesne_effects (id SERIAL PRIMARY KEY, FOREIGN KEY(stronghold_class_id) REFERENCES stronghold_classes(id), effect_description TEXT);"
)

CREATE_CLASS_FEATURE_IMPROVEMENTS_TABLE = (
    "CREATE TABLE IF NOT EXISTS class_feature_improvements (id SERIAL PRIMARY KEY, FOREIGN KEY(stronghold_class_id) REFERENCES stronghold_classes(id), improvement_name TEXT, improvement_description TEXT, improvement_uses INTEGER);"
)

CREATE_STRONGHOLD_TOUGHNESS_LEVELS_TABLE = (
    "CREATE TABLE IF NOT EXISTS stronghold_toughness_levels (id SERIAL PRIMARY KEY, level INTEGER, FOREIGN KEY(stronghold_class_id) REFERENCES stronghold_classes(id), stronghold_toughness INTEGER);"
)

CREATE_STRONGHOLD_CLASSES_TABLE = (
    "CREATE TABLE IF NOT EXISTS stronghold_classes (id SERIAL PRIMARY KEY, class_name TEXT, class_stronghold_name TEXT);"
)

CREATE_STRONGHOLD_SUBTYPES_TABLE = (
    "CREATE TABLE IF NOT EXISTS stronghold_subtypes (id SERIAL PRIMARY KEY, subtype_name TEXT);"
)

CREATE_STRONGHOLD_TYPES_TABLE = (
    "CREATE TABLE IF NOT EXISTS stronghold_types (id SERIAL PRIMARY KEY, type_name TEXT UNIQUE);"
)

CREATE_STRONGHOLD_TYPE_FEATURES_TABLE = (
    "CREATE TABLE IF NOT EXISTS stronghold_type_features (id SERIAL PRIMARY KEY, FOREIGN KEY(stronghold_type_id) REFERENCES stronghold_types(id), feature_name TEXT, feature_description TEXT);"
)

CREATE_STRONGHOLDS_TABLE = (
    "CREATE TABLE IF NOT EXISTS strongholds (id SERIAL PRIMARY KEY, FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE, stronghold_name TEXT, stronghold_level INTEGER, FOREIGN KEY(stronghold_type_id) REFERENCES stronghold_types(id), FOREIGN KEY(stronghold_subtype_id) REFERENCES stronghold_subtypes(id), FOREIGN KEY(stronghold_class_id) REFERENCES stronghold_classes(id),  created_at TIMESTAMP);"
)

INSERT_STRONGHOLD_TYPES = "INSERT INTO stronghold_types (type_name) VALUES ('keep'),('tower'),('temple'),('establishment'),('castle') RETURNING *;"

INSERT_USER_RETURN_ID = "INSERT INTO users (user_name, email, user_password, account_created) VALUES (%s, %s, %s, %s) RETURNING id;"

INSERT_STRONGHOLD = "INSERT INTO strongholds (stronghold_name, created_at) VALUES (%s, %s);"

GET_ALL_USERS = "SELECT * FROM users;"

GET_ALL_STRONGHOLD_TYPES = "SELECT * FROM stronghold_types;"

#Parse .env file and load all variables found within
load_dotenv()

app = Flask(__name__)
#This CANNOT be called url, it takes the env from smartpantry for some reason.
dburl = os.getenv("STRONGHOLD_DATABASE_URL")
connection = psycopg2.connect(dburl)

#root route
@app.get("/")
def default_route():
    return "hello world!"

#create and populate stronghold_types table
@app.post("/stronghold_types/")
def create_stronghold_types():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_STRONGHOLD_TYPES_TABLE)
            cursor.execute(INSERT_STRONGHOLD_TYPES)
            data = cursor.fetchall()
    return data, 201

#get all stronghold types
@app.get("/stronghold_types/")
def get_all_stronghold_types():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(GET_ALL_STRONGHOLD_TYPES)
            rows = cursor.fetchall()
    return {"message": "success!", "data": rows}, 200

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

if __name__ == "__main__":
    app.run()
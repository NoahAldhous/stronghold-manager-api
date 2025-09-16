from models.Class_stronghold_actions import CREATE_CLASS_STRONGHOLD_ACTIONS_TABLE, POPULATE_CLASS_STRONGHOLD_ACTIONS_TABLE, GET_ALL_CLASS_STRONGHOLD_ACTIONS, GET_STRONGHOLD_ACTIONS_BY_CLASS_ID, CLEAR_STRONGHOLD_ACTIONS_TABLE
from utils.db import query, execute

# CREATE STRONGHOLD ACTIONS TABLE
def create_class_stronghold_actions_table():
    res = execute(CREATE_CLASS_STRONGHOLD_ACTIONS_TABLE)
    
    if res:
        return{ "message" : "Table created" }, 200
    else:
        return{ "message" : "Could not create table" }, 404

# POPULATE STRONGHOLD ACTIONS TABLE
def populate_class_stronghold_actions_table():
    res = execute(POPULATE_CLASS_STRONGHOLD_ACTIONS_TABLE)
    
    if res:
        return{ "message" : "Table populated" }, 201
    else:
        return{ "message" :  "Could not populate table"}, 404
    
# GET ALL STRONGHOLD ACTIONS
def get_all_class_stronghold_actions():
    data = query(GET_ALL_CLASS_STRONGHOLD_ACTIONS, fetchone=False)
    
    if data:
        return{ "message" : "Success!", "data": data }, 200
    else:
        return{ "message" : "Could not fetch data" }, 404

# GET STRONGHOLD ACTIONS BY CLASS ID 
def get_class_stronghold_actions_by_class_id(class_id):
    data = query(GET_ALL_CLASS_STRONGHOLD_ACTIONS, (class_id,), fetchone=False)
    
    if data:
        return{ "message" : "Success!", "data": data }, 200
    else:
        return{ "message" : "Could not fetch data" }, 404

# DELETE ALL ROWS
def clear_class_stronghold_actions_table():
    res = execute(CLEAR_STRONGHOLD_ACTIONS_TABLE)
    
    if res:
        return{ "message" : "All rows deleted" }, 200
    else:
        return{ "message" :  "Could not populate table"}, 404
    
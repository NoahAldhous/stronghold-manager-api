from models.Stronghold_classes import CREATE_STRONGHOLD_CLASSES_TABLE, POPULATE_STRONGHOLD_CLASSES_TABLE, GET_ALL_STRONGHOLD_CLASSES, GET_STRONGHOLD_CLASS_BY_CLASS_NAME, GET_STRONGHOLD_CLASS_BY_ID, CLEAR_STRONGHOLD_CLASSES_TABLE
from utils.db import query, execute

# CREATE STRONGHOLD CLASSES TABLE 
def create_stronghold_classes_table():
    res = execute(CREATE_STRONGHOLD_CLASSES_TABLE)
    
    if res:
        return{ "message" : "Table created successfully" }, 200
    else: 
        return { "message" : "Could not created table"}, 404

# POPULATE STRONGHOLD CLASSES TABLE
def populate_stronghold_classes_table():
    res = execute(POPULATE_STRONGHOLD_CLASSES_TABLE)
    
    if res:
        return{ "message" : "Classes table populated" }, 201
    else:
        return{ "message" : "Could not populate table" }, 404

# GET ALL STRONGHOLD CLASSES
def get_all_stronghold_classes():
    data = query(GET_ALL_STRONGHOLD_CLASSES, fetchone=False)
    
    if data:
        return{ "message" : "Success!", "data": data }, 200
    else:
        return{ "message" : "Could not fetch data" }, 404

# GET STRONGHOLD CLASS BY CLASS NAME
def get_stronghold_class_by_class_name(class_name):
    data = query(GET_STRONGHOLD_CLASS_BY_CLASS_NAME, (class_name,), fetchone=True)
    
    if data:
        return{ "message" : "Success!", "data": data }, 200
    else:
        return{ "message" : "Could not fetch data" }, 404

# GET STRONGHOLD CLASS BY ID 
def get_stronghold_class_by_class_id(class_id):
    data = query(GET_STRONGHOLD_CLASS_BY_ID, (class_id,), fetchone=True)
    
    if data:
        return{ "message" : "Success!", "data": data }, 200
    else:
        return{ "message" : "Could not fetch data" }, 404

# DELETE ALL ROWS IN TABLE
def clear_stronghold_classes_table():
    res = execute(CLEAR_STRONGHOLD_CLASSES_TABLE)
    
    if res:
        return{ "message" : "All rows deleted" }, 200
    else:
        return{ "message" : "Something went wrong" }, 404
from models.Class_demesne_effects import CREATE_CLASS_DEMESNE_EFFECTS_TABLE, POPULATE_CLASS_DEMESNE_EFFECTS_TABLE, GET_ALL_CLASS_DEMESNE_EFFECTS, GET_CLASS_DEMESNE_EFFECTS_BY_CLASS_ID, CLEAR_CLASS_DEMESNE_EFFECTS_TABLE
from utils.db import query, execute

# CREATE CLASS DEMESNE EFFECTS TABLE
def create_class_demesne_effects_table():
    res = execute(CREATE_CLASS_DEMESNE_EFFECTS_TABLE)
    
    if res:
        return{ "message" : "Table created!" }, 200
    else:
        return{ "message" : "Could not create table"}, 404
    
# POPULATE CLASS DEMESNE EFFECTS TABLE
def populate_class_demesne_effects_table():
    res = execute(POPULATE_CLASS_DEMESNE_EFFECTS_TABLE)
    
    if res:
        return{ "message" : "Table populated!" }, 200
    else:
        return{ "message" : "Could not create table"}, 404

# GET ALL DEMESNE EFFECTS
def get_all_class_demesne_effects():
    data = query(GET_ALL_CLASS_DEMESNE_EFFECTS, fetchone=False)
    
    if data:
        return{ "message" : "success!", "data" : data}, 200
    else: 
        return{ "message" : "could not fetch data"}, 404

# GET DEMESNE EFFECTS BY CLASS ID
def get_class_demesne_effects_by_class_id(class_id):
    data = query(GET_CLASS_DEMESNE_EFFECTS_BY_CLASS_ID, (class_id,), fetchone=False)
    
    if data:
        return{ "message" : "success!", "data" : data}, 200
    else: 
        return{ "message" : "could not fetch data"}, 404


# DELETE ALL ROWS
def clear_class_demesne_effects_table():
    res = execute(CLEAR_CLASS_DEMESNE_EFFECTS_TABLE)
    
    if res:
        return{ "message" : "All rows deleted" }, 200
    else:
        return{ "message" : "Something went wrong"}, 404

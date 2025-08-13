from models.Stronghold_size_levels import CREATE_STRONGHOLD_SIZE_LEVELS_TABLE, INSERT_STRONGHOLD_SIZE_LEVEL, GET_ALL_STRONGHOLD_SIZE_LEVELS, GET_STRONGHOLD_SIZE_LEVEL_BY_TYPE_ID, GET_STRONGHOLD_SIZE_BY_LEVEL, UPDATE_STRONGHOLD_SIZE_LEVEL_BY_ID, DELETE_STRONGHOLD_SIZE_LEVEL_BY_ID
from utils.db import query, execute
from flask import request

#CREATE SIZE LEVELS TABLE
def create_stronghold_size_levels_table():
    res = execute(CREATE_STRONGHOLD_SIZE_LEVELS_TABLE)
    
    if res:
        return{"message" : "Table created"}, 200
    else:
        return{"message" : "Oops, an error occured"}, 404

#INSERT A SIZE LEVEL
def insert_new_stronghold_size_level():
    data = request.get_json()
    strongholdLevel = data["stronghold_level"]
    strongholdType = data["stronghold_type"]
    strongholdSize = data["stronghold_size"]
    execute(CREATE_STRONGHOLD_SIZE_LEVELS_TABLE)
    res = execute(INSERT_STRONGHOLD_SIZE_LEVEL, (strongholdLevel, strongholdType, strongholdSize,))
    
    if res:
        return {"message" : "new size level added successfully!"}, 201
    else: 
        return {"message" : "could not add size level"}, 404
    
#GET ALL SIZE LEVELS
def get_all_stronghold_size_levels():
    data = query(GET_ALL_STRONGHOLD_SIZE_LEVELS, fetchone=False)
    
    if data:
        return {"message" : "Success", "data" : data}, 200
    else:
        return {"message" : "Could not fetch data"}, 404

#GET LEVELS BY TYPE ID
def get_stronghold_size_levels_by_type_id(type_id):
    data = query(GET_STRONGHOLD_SIZE_LEVEL_BY_TYPE_ID, (type_id,), fetchone=False)
    
    if data:
        return {"message" : "Success!", "data" : data}, 200
    else:
        return {"message" : "Could not fetch data"}, 404

#GET SIZE BY LEVEL
def get_stronghold_size_by_level(level):
    data = query(GET_STRONGHOLD_SIZE_BY_LEVEL, (level,), fetchone=False)
    
    if data:
        return {"message" : "Success!", "data" : data}, 200
    else:
        return {"message" : "Could not fetch data"}, 404

#UPDATE SIZE LEVEL BY ID
def update_stronghold_size_level_by_id(level_id):
    data = request.get_json()
    strongholdSize = data["stronghold_size"]
    res = execute(UPDATE_STRONGHOLD_SIZE_LEVEL_BY_ID, (strongholdSize, level_id,))
    
    if res:
        return {"message" : "Item updated successfully"}, 200
    else:
        return {"message" : "Could not find item"}, 404

#DELETE SIZE LEVEL BY ID
def delete_stronghold_size_level_by_id(level_id):
    res = execute(DELETE_STRONGHOLD_SIZE_LEVEL_BY_ID, (level_id,))
    
    if res: 
        return {"message" : "Item deleted successfuly"}, 200
    else: 
        return {"message" : "Could not find item"}, 404
from models.Stronghold_toughness_levels import CREATE_STRONGHOLD_TOUGHNESS_LEVELS_TABLE, INSERT_STRONGHOLD_TOUGHNESS_LEVEL, GET_ALL_STRONGHOLD_TOUGHNESS_LEVELS, GET_STRONGHOLD_TOUGHNESS_BY_LEVEL, GET_STRONGHOLD_TOUGHNESS_LEVELS_BY_TYPE_ID, UPDATE_STRONGHOLD_TOUGHNESS_LEVEL_BY_ID, DELETE_STRONGHOLD_TOUGHNESS_LEVEL_BY_ID
from utils.db import query, execute
from flask import request

# CREATE TOUGHNESS LEVELS TABLE
def create_stronghold_toughness_levels_table():
    res = execute(CREATE_STRONGHOLD_TOUGHNESS_LEVELS_TABLE)
    
    if res:
        return{"message" : "Table created"}, 200
    else:
        return{"message" : "Oops, an error occured"}, 404

# INSERT A TOUGHNESS LEVEL
def insert_new_stronghold_toughness_level():
    data = request.get_json()
    strongholdType = data["stronghold_type"]
    strongholdLevel = data["stronghold_level"]
    strongholdToughness = data["stronghold_toughness"]
    execute(CREATE_STRONGHOLD_TOUGHNESS_LEVELS_TABLE)
    res = execute(INSERT_STRONGHOLD_TOUGHNESS_LEVEL, (strongholdLevel, strongholdType, strongholdToughness,))
    
    if res: 
        return {"message" : "new toughness level added successfully!"}, 201
    else: return {"message" : "could not add toughness level"}, 404

# GET ALL TOUGHNESS LEVELS
def get_all_stronghold_toughness_levels():
    data = query(GET_ALL_STRONGHOLD_TOUGHNESS_LEVELS, fetchone=False)
    
    if data:
            return{"message" : "Success!", "data" : data}, 200
    else:
        return{"message" : "Could not fetch data"}, 404

# GET TOUGHNESS LEVELS BY TYPE
def get_stronghold_toughness_levels_by_type_id(type_id):
    data = query(GET_STRONGHOLD_TOUGHNESS_LEVELS_BY_TYPE_ID, (type_id,), fetchone=False)
    
    if data:
            return{"message" : "Success!", "data" : data}, 200
    else:
        return{"message" : "Could not fetch data"}, 404

# GET TOUGHNESS BY LEVEL
def get_stronghold_toughness_by_level(level):
    data = query(GET_STRONGHOLD_TOUGHNESS_BY_LEVEL, (level,), fetchone=False)
    
    if data:
            return{"message" : "Success!", "data" : data}, 200
    else:
        return{"message" : "Could not fetch data"}, 404

# UPDATE TOUGHNESS LEVEL BY ID 
def update_stronghold_toughness_level_by_id(level_id):
    data = request.get_json()
    newToughness = data["toughness"]
    res = execute(UPDATE_STRONGHOLD_TOUGHNESS_LEVEL_BY_ID, (newToughness, level_id,))
    
    if res:
        return {"message" : "Item updated successfully"}, 200
    else:
        return {"message" : "Could not find item"}, 404

# DELETE TOUGHNESS LEVEL BY ID
def delete_stronghold_toughness_level_by_id(level_id):
    res = execute(DELETE_STRONGHOLD_TOUGHNESS_LEVEL_BY_ID, (level_id,))
    
    if res:
            return {"message" : "Item deleted successfuly"}, 200
    else:
        return {"message" : "Could not find item"}, 404

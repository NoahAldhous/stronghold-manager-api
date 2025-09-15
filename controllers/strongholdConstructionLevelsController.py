from models.Stronghold_construction_levels import CREATE_STRONGHOLD_CONSTRUCTION_LEVELS_TABLE, INSERT_STRONGHOLD_CONSTRUCTION_LEVEL, POPULATE_STRONGHOLD_CONSTRUCTION_LEVELS_TABLE, GET_ALL_STRONGHOLD_CONSTRUCTION_LEVELS, GET_STRONGHOLD_CONSTRUCTION_LEVELS_BY_TYPE_ID, GET_STRONGHOLD_CONSTRUCTION_BY_LEVEL, UPDATE_STRONGHOLD_CONSTRUCTION_LEVEL_BY_ID, DELETE_STRONGHOLD_CONSTRUCTION_LEVEL_BY_ID, CLEAR_STRONGHOLD_CONSTRUCTION_LEVELS_TABLE
from utils.db import query, execute
from flask import request

#CREATE CONSTRUCTION LEVELS TABLE
def create_stronghold_construction_levels_table():
    res = execute(CREATE_STRONGHOLD_CONSTRUCTION_LEVELS_TABLE)
    
    if res:
        return{"message" : "Table created"}, 200
    else:
        return{"message" : "Oops, an error occured"}, 404
    
#POPULATE CONSTRUCTION LEVELS TABLE
def populate_stronghold_levels_table():
    res = execute(POPULATE_STRONGHOLD_CONSTRUCTION_LEVELS_TABLE)
    
    if res:
        return {"message" "table populated"}, 201
    else:
        return {"message" : "something went wrong"}, 404

#INSERT A CONSTRUCTION LEVEL
def insert_new_stronghold_construction_level():
    data = request.get_json()
    strongholdLevel = data["stronghold_level"]
    strongholdType = data["stronghold_type"]
    costToBuild = data["cost_to_build"]
    timeToBuild = data["time_to_build"]
    moraleBonus = data["morale_bonus"]
    execute(CREATE_STRONGHOLD_CONSTRUCTION_LEVELS_TABLE)
    res = execute(INSERT_STRONGHOLD_CONSTRUCTION_LEVEL, (strongholdLevel, strongholdType, costToBuild, timeToBuild, moraleBonus,))
    
    if res: 
        return {"message" : "new construction level added successfully!"}, 201
    else: 
        return {"message" : "could not add construction level"}, 404
    
#GET ALL STRONGHOLD CONSTRUCTION LEVELS
def get_all_stronghold_construction_levels():
    data = query(GET_ALL_STRONGHOLD_CONSTRUCTION_LEVELS, fetchone=False)
    
    if data:
        return {"message" : "Success!", "data" : data}, 200
    else:
        return {"message" : "Could not fetch data"}, 404  

#GET CONSTRUCTION LEVEL BY TYPE ID
def get_stronghold_construction_levels_by_type_id(type_id):
    data = query(GET_STRONGHOLD_CONSTRUCTION_LEVELS_BY_TYPE_ID, (type_id,), fetchone=False)
    
    if data:
        return {"message" : "Success!", "data" : data}, 200
    else:
        return {"message" : "Could not fetch data"}, 404     

#GET CONSTRUCTION BY LEVEL
def get_stronghold_construction_by_level(level):
    data = query(GET_STRONGHOLD_CONSTRUCTION_BY_LEVEL, (level,), fetchone=False)
    
    if data:
        return {"message" : "Success!", "data" : data}, 200
    else:
        return {"message" : "Could not fetch data"}, 404
    
#UPDATE CONSTRUCTION LEVEL BY ID
def update_stronghold_construction_level_by_id(level_id):
    data = request.get_json()
    costToBuild = data["cost_to_build"]
    timeToBuild = data["time_to_build"]
    moraleBonus = data["morale_bonus"]
    res = execute(UPDATE_STRONGHOLD_CONSTRUCTION_LEVEL_BY_ID, (costToBuild, timeToBuild, moraleBonus, level_id,))
    
    if res:
        return {"message" : "Item updated successfully"}, 200
    else:
        return {"message" : "Could not find item"}, 404
    
#DELETE CONSTRUCTION LEVEL BY ID
def delete_stronghold_construction_level_by_id(level_id):
    res = execute(DELETE_STRONGHOLD_CONSTRUCTION_LEVEL_BY_ID, (level_id,))
    
    if res:
        return {"message" : "Item deleted successfuly"}, 200
    else:
        return {"message" : "Could not find item"}, 404 
    
#DELETE ALL ROWS
def clear_stronghold_construction_levels_table():
    res = execute(CLEAR_STRONGHOLD_CONSTRUCTION_LEVELS_TABLE)
    
    if res: 
        return {"message" : "All rows deleted"}, 200
    else:
        return {"message" : "Something went wrong"}, 404
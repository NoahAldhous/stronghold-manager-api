from models.Stronghold_types import CREATE_STRONGHOLD_TYPES_TABLE, INSERT_STRONGHOLD_TYPES, ADD_NEW_STRONGHOLD_TYPE, GET_ALL_STRONGHOLD_TYPES, GET_STRONGHOLD_TYPE_AND_FEATURES, UPDATE_STRONGHOLD_TYPE_BY_ID, DELETE_STRONGHOLD_TYPE_BY_ID
from utils.db import query, execute
from flask import request 

# CREATE STRONGHOLD TYPES
def create_stronghold_types_table():
    res = execute(CREATE_STRONGHOLD_TYPES_TABLE)
    
    if res:
        return {"message" : "Table created"}, 200
    else: 
        return {"message" : "Oops, an error occured"}, 404
    
# POPULATE STRONGHOLD TYPES
def populate_stronghold_types_table():
    execute(CREATE_STRONGHOLD_TYPES_TABLE)
    res = execute(INSERT_STRONGHOLD_TYPES)
    
    if res:
        return {"message" : "Success! Table populated"}, 200
    else:
        return {"message" : "An error occured"}, 404
    
# ADD NEW STRONGHOLD TYPE
def add_new_stronghold_type():
    data = request.get_json()
    typeName = data["name"]
    newType = query(ADD_NEW_STRONGHOLD_TYPE, (typeName,), fetchone=True)

    if newType:
        return {"message": "Success!", "New type added": newType}
    else:
        return {"message": "Something went wrong"}

# GET ALL STRONGHOLD TYPES
def get_all_stronghold_types():
    data = query(GET_ALL_STRONGHOLD_TYPES)
    
    if data:
        return {"message" : "Success!", "data": data}, 201
    else:
        return {"message" : "Something went wrong"}, 404

# GET STRONGHOLD TYPE + INFO BY ID
def get_stronghold_type_and_features_by_id(id):
    data = query(GET_STRONGHOLD_TYPE_AND_FEATURES, (id,), fetchone=True)
    
    if data:
        return {"message": "success!", "data": data}, 200
    else:
        return {"message": "could not find type"}, 400

# UPDATE STRONGHOLD TYPE
def update_stronghold_type_by_id(type_id):
    data = request.get_json()
    newTypeName = data["name"]
    res = execute(UPDATE_STRONGHOLD_TYPE_BY_ID, (newTypeName, type_id,))
    
    if res:
        return {"message" : "Item updated successfully"}, 200
    else:
        return {"message" : "Could not find item"}, 404

# DELETE STRONGHOLD TYPE
def delete_stronghold_type_by_id(type_id):
    res = execute(DELETE_STRONGHOLD_TYPE_BY_ID, (type_id,))
    
    if res:
        return {"message" : "Item deleted successfuly"}, 200
    else:
        return {"message" : "Could not find item"}, 404
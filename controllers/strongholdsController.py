from models.Strongholds import CREATE_STRONGHOLDS_TABLE, INSERT_STRONGHOLD_RETURN_ID, GET_STRONGHOLD_BY_ID, GET_STRONGHOLDS_BY_USER_ID, DELETE_STRONGHOLDS_TABLE, GET_STRONGHOLD_BY_ID_RETURN_ALL_STRONGHOLD_DATA
from utils.db import query, execute
from flask import request
from datetime import date

#CREATE STRONGHOLDS TABLE
def create_strongholds_table():
    res = execute(CREATE_STRONGHOLDS_TABLE)
    
    if res:
        return {"message" : "Table created"}, 200
    else: 
        return {"message" : "Oops, an error occured"}, 404

#INSERT STRONGHOLD
def insert_stronghold():
    data = request.get_json()
    userId = data["user_id"]
    strongholdName = data["stronghold_name"]
    ownerName = data["owner_name"]
    strongholdLevel = data["stronghold_level"]
    strongholdType = data["stronghold_type"]
    createdAt = date.today()
    execute(CREATE_STRONGHOLDS_TABLE)
    res = execute(INSERT_STRONGHOLD_RETURN_ID, (userId, strongholdName, ownerName, strongholdLevel, strongholdType, createdAt,))
    
    if res:
        return {"message" : "Success! Stronghold added", "id" : res}, 201
    else:
        return {"message" : "An error occured"}, 404

#GET STRONGHOLDS BY USER ID
def get_strongholds_by_user_id(id):
    data = query(GET_STRONGHOLDS_BY_USER_ID, (id,), fetchone=False)
    
    if data:
        return {"message" : "Success!", "data" : data}, 200
    else:
        return {"message" : "Could not fetch data"}, 404
    
#GET STRONGHOLD BY ID
def get_stronghold_by_id(id):
    data = query(GET_STRONGHOLD_BY_ID, (id,), fetchone=True)
    
    if data:
        return {"message" : "Success!", "data" : data}, 200
    else:
        return {"message" : "Could not fetch data"}, 404
    
#GET STRONGHOLD BY ID, RETURN ALL STRONGHOLD DATA
def get_stronghold_by_id_return_all_stronghold_data(id):
    data = query(GET_STRONGHOLD_BY_ID_RETURN_ALL_STRONGHOLD_DATA, (id,), fetchone=True)
    
    if data:
        return {"message" : "Success!", "data" : data}, 200
    else:
        return {"message" : "Could not fetch data"}, 404
    
#DELETE STRONGHOLDS TABLE
def delete_strongholds_table():
    res = execute(DELETE_STRONGHOLDS_TABLE)
    
    if res: 
        return {"message" : "table deleted"}, 200
    else:
        return {"message" : "table not found"}, 404
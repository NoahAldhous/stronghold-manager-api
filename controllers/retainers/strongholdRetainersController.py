from models.Retainers.Stronghold_Retainers import CREATE_STRONGHOLD_RETAINERS_TABLE, ADD_STRONGHOLD_RETAINER, GET_RETAINERS_BY_STRONGHOLD_ID, GET_STRONGHOLD_RETAINER_BY_ID
from utils.db import query, execute
from flask import request

# CREATE STRONGHOLD RETAINERS TABLE
def create_stronghold_retainers_table():
    res = execute(CREATE_STRONGHOLD_RETAINERS_TABLE)
    
    if res:
        return { "message" : "table created" }, 200
    else: 
        return { "message" : "error, could not create table" }, 404
    
# ADD A STRONGHOLD RETAINER
def add_stronghold_retainer():
    data = request.get_json()
    
    individual_name = data["individualName"]
    stronghold_id = data["strongholdId"]
    retainer_name = data["retainer"]
    ancestry_name = data["ancestry"]
    retainer_level = data["level"]
    health_levels_lost = data["healthLevelsLost"]
    
    res = query(ADD_STRONGHOLD_RETAINER, (individual_name, stronghold_id, retainer_name, ancestry_name, retainer_level, health_levels_lost), fetchone=True)
    
    if res:
        return {"message" : "stronghold retainer added", "id" : res["id"]}, 201
    else:
        return {"message" : "could not add stronghold retainer"}, 404
    
def get_stronghold_retainers_by_stronghold_id(stronghold_id):
    data = query(GET_RETAINERS_BY_STRONGHOLD_ID, (stronghold_id,), fetchone=False)
    
    if data:
        return {"message" : "success!", "retainers" : data}, 200
    else:
        return {"message" : "could not fetch stronghold retainers"}, 404

def get_stronghold_retainer_by_id(retainer_id):
    data = query(GET_STRONGHOLD_RETAINER_BY_ID, (retainer_id,), fetchone=True)
    
    if data:
        return {"message" : "success!", "retainer" : data}, 200
    else:
        return {"message" : "could not find stronghold retainer"}, 404
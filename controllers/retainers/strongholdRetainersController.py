from models.Retainers.Stronghold_Retainers import CREATE_STRONGHOLD_RETAINERS_TABLE, ADD_STRONGHOLD_RETAINER
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
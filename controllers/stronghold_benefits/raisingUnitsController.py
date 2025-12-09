from models.Stronghold_benefits.Raising_units import UPDATE_STRONGHOLD_RAISING_UNITS_STATUS_BY_STRONGHOLD_ID, ADD_UNIT_RAISED, CREATE_RAISING_UNITS_TABLE, CREATE_UNITS_RAISED_TABLE, CREATE_STRONGHOLD_RAISING_UNITS_STATUS_TABLE, GET_STRONGHOLD_RAISING_UNITS_STATUS_BY_STRONGHOLD_ID, POPULATE_RAISING_UNITS_TABLE, GET_UNITS_RAISED_BY_KEEP_TYPE
from utils.db import query, execute
from flask import request
# from datetime import date

# CREATE RAISING UNITS TABLE
def create_raising_units_table():
    res = execute(CREATE_RAISING_UNITS_TABLE)
    
    if res:
        return {"message" : "Table created"}, 200
    else: 
        return {"message" : "Oops, an error occured"}, 404
    
# CREATE UNITS RAISED TABLE
def create_units_raised_table():
    res = execute(CREATE_UNITS_RAISED_TABLE)
    
    if res:
            return {"message" : "Table created"}, 200
    else: 
        return {"message" : "Oops, an error occured"}, 404
    

# CREATE STRONGHOLD RAISING UNITS STATUS TABLE
def create_stronghold_raising_units_status_table():
    res = execute(CREATE_STRONGHOLD_RAISING_UNITS_STATUS_TABLE)
    
    if res:
            return {"message" : "Table created"}, 200
    else: 
        return {"message" : "Oops, an error occured"}, 404

# ADD A RAISED UNIT
def add_unit_raised():
    data = request.get_json()
    stronghold_id = data["strongholdId"]
    unit_id = data["unitId"]
    raising_unit_id = data["raisingUnitId"]
    
    res = query(ADD_UNIT_RAISED, (stronghold_id, unit_id, raising_unit_id,), fetchone=True)
    
    if res:
        return{ "message" : "Successfully added raised unit"}, 200
    else:
        return{ "message" : "Error, could not add raised unit"}, 404
    
# GET STATUS BY STRONGHOLD
def get_stronghold_raising_units_status_by_stronghold_id(stronghold_id):
    data = query(GET_STRONGHOLD_RAISING_UNITS_STATUS_BY_STRONGHOLD_ID, (stronghold_id,), fetchone=True)
    
    if data:
        return{ "message" : "Success", "status": data}, 200
    else: 
        return{ "message" : "Could not fetch status" }, 404
    
# UPDATE STRONGHOLD RAISING UNITS STATUS
def update_stronghold_raising_units_status_by_stronghold_id(stronghold_id):
    data = request.get_json()
    current_units = data["currentUnits"]
    has_raised_all_units = data["hasRaisedAllUnits"]
    
    res = query(UPDATE_STRONGHOLD_RAISING_UNITS_STATUS_BY_STRONGHOLD_ID, (current_units, has_raised_all_units, stronghold_id), fetchone=True)
    
    if res:
        return{"message" : "Success", "updatedRow" : res}, 200
    else:
        return{"message" : "Error, could not updated"}, 404
         
# POPULATE RAISING UNITS TABLE
def populate_raising_units_table():
    res = execute(POPULATE_RAISING_UNITS_TABLE)
    
    if res:
        return{ "message" : "Table populated!" }, 200
    else:
        return{ "message" : "Could not populate table" }, 404
    
# GET UNITS BY KEEP TYPE
def get_units_raised_by_keep_type(keep_type):
    data = query(GET_UNITS_RAISED_BY_KEEP_TYPE, (keep_type,), fetchone=False)
    
    if data:
        return{ "message" : "Success!", "units" : data}, 200
    else:
        return{ "message" : "Could not fetch data"}, 404
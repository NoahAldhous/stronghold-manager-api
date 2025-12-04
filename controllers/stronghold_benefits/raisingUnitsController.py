from models.Stronghold_benefits.Raising_units import CREATE_RAISING_UNITS_TABLE, CREATE_UNITS_RAISED_TABLE, CREATE_STRONGHOLD_RAISING_UNITS_STATUS_TABLE, POPULATE_RAISING_UNITS_TABLE, GET_UNITS_RAISED_BY_KEEP_TYPE
from utils.db import query, execute
# from flask import request
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
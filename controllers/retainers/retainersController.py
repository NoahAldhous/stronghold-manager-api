from models.Retainers.Retainers import CREATE_RETAINERS_TABLE, POPULATE_RETAINERS_TABLE, GET_ALL_RETAINERS
from utils.db import query, execute

# CREATE RETAINERS TABLE
def create_retainers_table():
    res = execute(CREATE_RETAINERS_TABLE)
    
    if res:
        return { "message" : "table created" }, 200
    else: 
        return { "message" : "error, could not create table" }, 404
    
# POPULATE RETAINERS TABLE
def populate_retainers_table():
    res = execute(POPULATE_RETAINERS_TABLE)
    
    if res:
            return { "message" : "table populated" }, 200
    else:
        return { "message" : "error, could not populate table" }, 404
    
# GET ALL RETAINERS
def get_all_retainers():
    data = query(GET_ALL_RETAINERS, fetchone=False)
    
    if data:
            return { "message" : "success!", "retainers" : data }, 200
    else:
        return { "message" : "error, could not fetch retainers" }, 404
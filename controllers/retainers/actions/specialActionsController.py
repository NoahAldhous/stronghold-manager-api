from models.Retainers.Actions.Special_actions import CREATE_SPECIAL_ACTIONS_TABLE, POPULATE_SPECIAL_ACTIONS_TABLE
from utils.db import execute

# CREATE SPECIAL ACTIONS TABLE
def create_special_actions_table():
    res = execute(CREATE_SPECIAL_ACTIONS_TABLE)
    
    if res:
        return { "message" : "table created" }, 200
    else: 
        return { "message" : "error, could not create table" }, 404
    
# POPULATE SPECIAL ACTIONS TABLE
def populate_special_actions_table():
    res = execute(POPULATE_SPECIAL_ACTIONS_TABLE)
    
    if res:
            return { "message" : "table populated" }, 200
    else:
        return { "message" : "error, could not populate table" }, 404
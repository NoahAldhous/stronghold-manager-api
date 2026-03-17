from models.Retainers.Stronghold_Retainers import CREATE_STRONGHOLD_RETAINERS_TABLE
from utils.db import execute

# CREATE STRONGHOLD RETAINERS TABLE
def create_stronghold_retainers_table():
    res = execute(CREATE_STRONGHOLD_RETAINERS_TABLE)
    
    if res:
        return { "message" : "table created" }, 200
    else: 
        return { "message" : "error, could not create table" }, 404
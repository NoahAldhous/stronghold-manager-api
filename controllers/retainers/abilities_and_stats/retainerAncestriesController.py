from models.Retainers.Abilities_and_Stats.Retainer_ancestries import CREATE_RETAINER_ANCESTRIES_TABLE, POPULATE_RETAINER_ANCESTRIES_TABLE
from utils.db import execute

# CREATE RETAINER ANCESTRIES TABLE
def create_retainer_ancestries_table():
    res = execute(CREATE_RETAINER_ANCESTRIES_TABLE)
    
    if res:
        return { "message" : "table created" }, 200
    else: 
        return { "message" : "error, could not create table" }, 404
    
# POPULATE ABILITIES TABLE
def populate_retainer_ancestries_table():
    res = execute(POPULATE_RETAINER_ANCESTRIES_TABLE)
    
    if res:
            return { "message" : "table populated" }, 200
    else:
        return { "message" : "error, could not populate table" }, 404
    
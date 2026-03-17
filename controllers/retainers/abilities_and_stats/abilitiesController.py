from models.Retainers.Abilities_and_Stats.Abilities import CREATE_ABILIITIES_TABLE, POPULATE_ABILITIES_TABLE
from utils.db import execute

# CREATE ABILITIES TABLE
def create_abilities_table():
    res = execute(CREATE_ABILIITIES_TABLE)
    
    if res:
        return { "message" : "table created" }, 200
    else: 
        return { "message" : "error, could not create table" }, 404
    
# POPULATE ABILITIES TABLE
def populate_abilities_table():
    res = execute(POPULATE_ABILITIES_TABLE)
    
    if res:
            return { "message" : "table populated" }, 200
    else:
        return { "message" : "error, could not populate table" }, 404
    

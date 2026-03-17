from models.Retainers.Actions.Retainer_spells import CREATE_RETAINER_SPELLS_TABLE, POPULATE_RETAINER_SPELL_SPELLS_TABLE
from utils.db import execute

# CREATE RETAINER SPELLS TABLE
def create_retainer_spells_table():
    res = execute(CREATE_RETAINER_SPELLS_TABLE)
    
    if res:
        return { "message" : "table created" }, 200
    else: 
        return { "message" : "error, could not create table" }, 404
    
# POPULATE RETAINER SPELLS TABLE
def populate_retainer_spells_table():
    res = execute(POPULATE_RETAINER_SPELL_SPELLS_TABLE)
    
    if res:
            return { "message" : "table populated" }, 200
    else:
        return { "message" : "error, could not populate table" }, 404
    

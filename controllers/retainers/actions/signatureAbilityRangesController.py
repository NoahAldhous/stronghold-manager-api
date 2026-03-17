from models.Retainers.Actions.Signature_ability_ranges import CREATE_SIGNATURE_ABILITY_RANGES_TABLE, POPULATE_SIGNATURE_ABILITY_RANGES_TABLE
from utils.db import execute

# CREATE SIGNATURE ABILITY RANGES TABLE
def create_signature_ability_ranges_table():
    res = execute(CREATE_SIGNATURE_ABILITY_RANGES_TABLE)
    
    if res:
        return { "message" : "table created" }, 200
    else: 
        return { "message" : "error, could not create table" }, 404
    
# POPULATE SIGNATURE ABILITY RANGES TABLE
def populate_signature_ability_ranges_table():
    res = execute(POPULATE_SIGNATURE_ABILITY_RANGES_TABLE)
    
    if res:
            return { "message" : "table populated" }, 200
    else:
        return { "message" : "error, could not populate table" }, 404

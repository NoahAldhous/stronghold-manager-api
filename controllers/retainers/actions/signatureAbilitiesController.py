from models.Retainers.Actions.Signature_abilities import CREATE_SIGNATURE_ABILITIES_TABLE, POPULATE_SIGNATURE_ABILITIES_TABLE
from utils.db import execute

# CREATE SIGNATURE ABILITIES TABLE
def create_signature_abilities_table():
    res = execute(CREATE_SIGNATURE_ABILITIES_TABLE)
    
    if res:
        return { "message" : "table created" }, 200
    else: 
        return { "message" : "error, could not create table" }, 404
    
# POPULATE SIIGNATURE ABILITIES TABLE
def populate_signature_abilities_table():
    res = execute(POPULATE_SIGNATURE_ABILITIES_TABLE)
    
    if res:
            return { "message" : "table populated" }, 200
    else:
        return { "message" : "error, could not populate table" }, 404
    

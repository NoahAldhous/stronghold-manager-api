from models.Retainers.Abilities_and_Stats.Classes import CREATE_CLASSES_TABLE, POPULATE_CLASSES_TABLE
from utils.db import execute

# CREATE CLASSES TABLE
def create_classes_table():
    res = execute(CREATE_CLASSES_TABLE)
        
    if res:
        return { "message" : "table created" }, 200
    else: 
        return { "message" : "error, could not create table" }, 404
    
# POPULATE ABILITIES TABLE
def populate_classes_table():
    res = execute(POPULATE_CLASSES_TABLE)
    
    if res:
            return { "message" : "table populated" }, 200
    else:
        return { "message" : "error, could not populate table" }, 404
    
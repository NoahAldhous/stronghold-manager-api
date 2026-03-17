
from models.Retainers.Abilities_and_Stats.Retainer_armour_classes import CREATE_RETAINER_ARMOUR_CLASSES_TABLE, POPULATE_RETAINER_ARMOUR_CLASSES_TABLE
from utils.db import execute

# CREATE ABILITIES TABLE
def create_retainer_armour_classes_table():
    res = execute(CREATE_RETAINER_ARMOUR_CLASSES_TABLE)
    
    if res:
        return { "message" : "table created" }, 200
    else: 
        return { "message" : "error, could not create table" }, 404
    
# POPULATE ABILITIES TABLE
def populate_retainer_armour_classes_table():
    res = execute(POPULATE_RETAINER_ARMOUR_CLASSES_TABLE)
    
    if res:
            return { "message" : "table populated" }, 200
    else:
        return { "message" : "error, could not populate table" }, 404
    
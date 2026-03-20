from models.Retainers.Abilities_and_Stats.Retainer_class_saves_relations import CREATE_RETAINER_CLASS_SAVES_RELATIONS_TABLE, POPULATE_RETAINER_CLASS_SAVES_RELATIONS_TABLE
from utils.db import execute

# CREATE RETAINER CLASS SAVES RELATIONS TABLE
def create_retainer_class_saves_relations_table():
    res = execute(CREATE_RETAINER_CLASS_SAVES_RELATIONS_TABLE)
    
    if res:
        return { "message" : "table created" }, 200
    else: 
        return { "message" : "error, could not create table" }, 404
    
# POPULATE RETAINER CLASS SAVES RELATIONS TABLE
def populate_retainer_class_saves_relations_table():
    res = execute(POPULATE_RETAINER_CLASS_SAVES_RELATIONS_TABLE)
    
    if res:
            return { "message" : "table populated" }, 200
    else:
        return { "message" : "error, could not populate table" }, 404
    
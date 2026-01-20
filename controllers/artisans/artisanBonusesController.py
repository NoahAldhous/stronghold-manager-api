from models.Artisans.Artisan_bonuses import CREATE_ARTISAN_BONUSES_TABLE, POPULATE_ARTISAN_BONUSES_TABLE
from utils.db import execute

# CREATE ARTISAN BONUSES TABLE
def create_artisan_bonuses_table():
    res = execute(CREATE_ARTISAN_BONUSES_TABLE)
    
    if res:
        return { "message" : "table created" }, 200
    else: 
        return{ "message" : "error, could not create table" }, 404
    
# POPULATE ARTISAN BONUSES TABLE
def populate_artisan_bonuses_table():
    res = execute(POPULATE_ARTISAN_BONUSES_TABLE)
    
    if res:
        return { "message" : "table populated" }, 200
    else :
        return { "message" : "error, could not populate table" }, 404

    
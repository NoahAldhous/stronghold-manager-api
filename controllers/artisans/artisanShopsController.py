from models.Artisans.Artisan_shops import CREATE_ARTISAN_SHOPS_TABLE, POPULATE_ARTISAN_SHOPS_TABLE
from utils.db import execute

# CREATE ARTISAN SHOPS TABLE
def create_artisan_shops_table():
    res = execute(CREATE_ARTISAN_SHOPS_TABLE)
    
    if res:
        return { "message" : "table created" }, 200
    else: 
        return { "message" : "error, could not create table" }, 404
    
# POPULATE ARTISAN SHOPS TABLE
def populate_artisan_shops_table():
    res = execute(POPULATE_ARTISAN_SHOPS_TABLE)
    
    if res:
        return { "message" : "table populated" }, 200
    else:
        return { "message" : "error, could not populate table" }, 404
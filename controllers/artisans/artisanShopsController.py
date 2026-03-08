from models.Artisans.Artisan_shops import CREATE_ARTISAN_SHOPS_TABLE, POPULATE_ARTISAN_SHOPS_TABLE, GET_ARTISAN_SHOPS
from utils.db import execute, query

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
    
# GET ALL ARTISAN SHOPS
def get_all_artisan_shops():
    data = query(GET_ARTISAN_SHOPS, fetchone=False)
    
    if data:
        return { "message" : "success", "artisanShops" : data}, 200
    else:
        return { "message" : "error, could not fetch artisans"}, 404
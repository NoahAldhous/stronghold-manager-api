from models.Artisans.Artisan_upgrade_costs import CREATE_ARTISAN_UPGRADE_COSTS_TABLE, POPULATE_ARTISAN_UPGRADE_COSTS_TABLE
from utils.db import execute

# CREATE ARTISAN UPGRADE COSTS TABLE
def create_artisan_upgrade_costs_table():
    res = execute(CREATE_ARTISAN_UPGRADE_COSTS_TABLE)
    
    if res:
        return { "message" : "table created" }, 200
    else: 
        return { "message" : "error, could not create table" }, 404
    
# POPULATE ARTISAN UPGRADE COSTS TABLE
def populate_artisan_upgrade_costs_table():
    res = execute(POPULATE_ARTISAN_UPGRADE_COSTS_TABLE)
    
    if res:
        return { "message" : "table populated" }, 200
    else:
        return { "message" : "error, could not populate table" }, 404
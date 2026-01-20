from models.Artisans.Stronghold_Artisans import CREATE_STRONGHOLD_ARTISANS_TABLE
from utils.db import execute

# CREATE STRONGHOLD ARTISANS TABLE
def create_stronghold_artisans_table():
    res = execute(CREATE_STRONGHOLD_ARTISANS_TABLE)
    
    if res:
        return { "message" : "table created" }, 200
    else:
        return { "message" : "error, could not create table" }, 404
    
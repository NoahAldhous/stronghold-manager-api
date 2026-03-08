from models.Artisans.Stronghold_Artisans import CREATE_STRONGHOLD_ARTISANS_TABLE, GET_STRONGHOLD_ARTISANS_BY_STRONGHOLD_ID
from utils.db import query, execute

# CREATE STRONGHOLD ARTISANS TABLE
def create_stronghold_artisans_table():
    res = execute(CREATE_STRONGHOLD_ARTISANS_TABLE)
    
    if res:
        return { "message" : "table created" }, 200
    else:
        return { "message" : "error, could not create table" }, 404
    
# GET ARTISANS BY STRONGHOLD ID
def get_all_artisans_by_stronghold_id(stronghold_id):
    data = query(GET_STRONGHOLD_ARTISANS_BY_STRONGHOLD_ID, (stronghold_id,), fetchone=True)
        
    if data:
        return {"message" : "Success!", "artisans" : data}, 200
    else:
        return {"message" : "could not fetch data"}, 404
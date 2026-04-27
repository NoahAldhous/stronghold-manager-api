from models.Artisans.Stronghold_Artisans import CREATE_STRONGHOLD_ARTISANS_TABLE, GET_STRONGHOLD_ARTISANS_BY_STRONGHOLD_ID, INSERT_STRONGHOLD_ARTISAN, UPDATE_STRONGHOLD_ARTISAN, DELETE_STRONGHOLD_ARTISANS_TABLE, DELETE_STRONGHOLD_ARTISAN
from utils.db import query, execute
from flask import request

# CREATE STRONGHOLD ARTISANS TABLE
def create_stronghold_artisans_table():
    res = execute(CREATE_STRONGHOLD_ARTISANS_TABLE)
    
    if res:
        return { "message" : "table created" }, 200
    else:
        return { "message" : "error, could not create table" }, 404
    
# INSERT STRONGHOLD ARTISAN
def insert_stronghold_artisan():
    data = request.get_json()
    stronghold_id = data["strongholdId"]
    artisan_name = data["artisan"]
    shop_level = data["level"]
    
    res = execute(INSERT_STRONGHOLD_ARTISAN, (stronghold_id, artisan_name, shop_level)) 
    
    if res:
        return {"message" : "Artisan added successfully!"}, 200
    else:
        return {"message" : "Error- could not add artisan."}, 404

# UPDATE STRONGHOLD ARTISAN
def update_stronghold_artisan():
    data = request.get_json()
    new_level = data["level"]
    stronghold_id = data["strongholdId"]
    artisan_name = data["artisan"]
    
    row = execute(UPDATE_STRONGHOLD_ARTISAN, (new_level, stronghold_id, artisan_name))
    
    if row:
        return {"message" : "Successfully updated artisan", "artisan" : row}, 200
    else:
        return{"message" : "Error- could not update artisan"}, 404
    

# GET ARTISANS BY STRONGHOLD ID
def get_all_artisans_by_stronghold_id(stronghold_id):
    data = query(GET_STRONGHOLD_ARTISANS_BY_STRONGHOLD_ID, (stronghold_id,), fetchone=False)
        
    if data:
        return {"message" : "Success!", "artisans" : data}, 200
    else:
        return {"message" : "could not fetch data"}, 404

# DELETE STRONGHOLD ARTISAN
def delete_stronghold_artisan(artisan_id):
    data = query(DELETE_STRONGHOLD_ARTISAN, (artisan_id,), fetchone=True)
    
    if data:
        return {"message" : "Success!", "artisanId" : data}, 200
    else:
        return {"message" : "could not delete artisan"}, 404
    
# DELETE STRONGHOLD ARTISAN TABLE
def delete_stronghold_artisans_table():
    res = execute(DELETE_STRONGHOLD_ARTISANS_TABLE)
    
    if res:
            return { "message" : "table delete" }, 200
    else:
        return { "message" : "error, could not delete table" }, 404
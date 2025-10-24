from models.Units.Ancestry_trait_relations import CREATE_ANCESTRY_TRAIT_RELATIONS_TABLE, POPULATE_ANCESTRY_TRAIT_RELATIONS_TABLE
from models.Units.Unit_ancestries import CREATE_UNIT_ANCESTRIES_TABLE, POPULATE_UNIT_ANCESTRIES_TABLE
from models.Units.Unit_equipment_levels import CREATE_UNIT_EQUIPMENT_LEVELS_TABLE, POPULATE_UNIT_EQUIPMENT_LEVELS_TABLE
from models.Units.Unit_experience_levels import CREATE_UNIT_EXPERIENCE_LEVELS_TABLE, POPULATE_UNIT_EXPERIENCE_LEVELS_TABLE
from models.Units.Unit_size_levels import CREATE_UNIT_SIZE_LEVELS_TABLE, POPULATE_UNIT_SIZE_LEVELS_TABLE, CLEAR_UNIT_SIZE_LEVELS_TABLE
from models.Units.Unit_traits import CREATE_UNIT_TRAITS_TABLE, POPULATE_UNIT_TRAITS_TABLE
from models.Units.Unit_types import CREATE_UNIT_TYPES_TABLE, POPULATE_UNIT_TYPES_TABLE, GET_ALL_UNIT_TYPES
from models.Units.Units import CREATE_UNITS_TABLE, ADD_UNIT, GET_UNITS_BY_USER_ID, GET_UNITS_BY_USER_AND_STRONGHOLD_ID
from utils.db import execute, query
from flask import request
from datetime import date

# CREATE UNITS TABLE
def create_units_table():
    res = execute(CREATE_UNITS_TABLE)
    
    if res:
        return{ "message" : "Table created!"}, 200
    else:
        return{ "message" : "Could not create table" }, 404

# ADD NEW UNIT
def add_unit():
    data = request.get_json()
    user_id = data["user_id"]
    unit_name = data["unit_name"]
    stronghold_id = data["stronghold_id"]
    ancestry = data["ancestry"]
    experience = data["experience"]
    equipment = data["equipment"]
    unit_type = data["unit_type"]
    size_level = data["size_level"]
    casualties = data["casualties"]
    mercenary = data["mercenary"]
    created_at = date.today()
    
    res = query(
            ADD_UNIT, 
            (
                user_id, 
                unit_name, 
                stronghold_id, 
                ancestry, 
                experience,
                equipment,
                unit_type,
                size_level,
                casualties,
                mercenary,
                created_at
            ), fetchone=True)
    
    if res:
        return {"message" : "Success! Stronghold added", "id" : res["id"]}, 201
    else:
        return {"message" : "An error occured"}, 404

# GET UNIT BY USER ID
def get_units_by_user_id(id):
    data = query(GET_UNITS_BY_USER_ID, (id,), fetchone=False)
    
    if data is None:
        return {"message" : "could not fetch data"}, 404
    else:
        return {"message" : "Success!", "units" : data}, 200
    
# GET UNIT BY USER AND STRONGHOLD ID
def get_units_by_user_and_stronghold_id(user_id, stronghold_id):
    data = query(GET_UNITS_BY_USER_AND_STRONGHOLD_ID, (user_id, stronghold_id,), fetchone=False)
    
    if data is None: #This ensures that if the query succeeds BUT no rows are found, it still returns an empty array rather than throwing an error.
        return {"message" : "could not fetch data"}, 404 
    else:
        return {"message" : "Success!", "units" : data}, 200
    
# GET ALL UNIT TYPES
def get_all_unit_types():
    data = query(GET_ALL_UNIT_TYPES, fetchone=False)
    
    if data:
        return{ "message" : "Success!", "types" : data}, 200
    else:
        return{ "message" : "Could not fetch data"}, 404

# CREATE ANCESTRY-TRAIT RELATIONS TABLE
def create_ancestry_trait_relations_table():
    res = execute(CREATE_ANCESTRY_TRAIT_RELATIONS_TABLE)
    
    if res:
        return{ "message" : "Table created!"}, 200
    else:
        return{ "message" : "Could not create table" }, 404

# POPULATE ANCESTRY-TRAIT RELATIONS TABLE
def populate_ancestry_trait_relations_table():
    res = execute(POPULATE_ANCESTRY_TRAIT_RELATIONS_TABLE)
    
    if res:
        return{ "message" : "Table populated!" }, 200
    else:
        return{ "message" : "Could not populate table" }, 404
 
# CREATE UNIT ANCESTRIES TABLE
def create_unit_ancestries_table():
    res = execute(CREATE_UNIT_ANCESTRIES_TABLE)
    
    if res:
        return{ "message" : "Table created!"}, 200
    else:
        return{ "message" : "Could not create table" }, 404
    
# POPULATE UNIT ANCESTRIES TABLE
def populate_unit_ancestries_table():
    res = execute(POPULATE_UNIT_ANCESTRIES_TABLE)
    
    if res:
        return{ "message" : "Table populated!" }, 200
    else:
        return{ "message" : "Could not populate table" }, 404
 

# CREATE UNIT EQUIPMENT LEVELS TABLE
def create_unit_equipment_levels_table():
    res = execute(CREATE_UNIT_EQUIPMENT_LEVELS_TABLE)
    
    if res:
        return{ "message" : "Table created!"}, 200
    else:
        return{ "message" : "Could not create table" }, 404
    
# POPULATE UNIT EQUIPMENT LEVELS TABLE
def populate_unit_equipment_levels_table():
    res = execute(POPULATE_UNIT_EQUIPMENT_LEVELS_TABLE)
    
    if res:
        return{ "message" : "Table populated!" }, 200
    else:
        return{ "message" : "Could not populate table" }, 404
 

# CREATE UNIT EXPERIENCE LEVELS TABLE
def create_unit_experience_levels_table():
    res = execute(CREATE_UNIT_EXPERIENCE_LEVELS_TABLE)
    
    if res:
        return{ "message" : "Table created!"}, 200
    else:
        return{ "message" : "Could not create table" }, 404
    
# POPULATE UNIT EXPERIENCE LEVELS TABLE
def populate_unit_experience_levels_table():
    res = execute(POPULATE_UNIT_EXPERIENCE_LEVELS_TABLE)
    
    if res:
        return{ "message" : "Table populated!" }, 200
    else:
        return{ "message" : "Could not populate table" }, 404
 

# CREATE UNIT SIZE LEVELS TABLE
def create_unit_size_levels_table():
    res = execute(CREATE_UNIT_SIZE_LEVELS_TABLE)
    
    if res:
        return{ "message" : "Table created!"}, 200
    else:
        return{ "message" : "Could not create table" }, 404
    
# POPULATE UNIT SIZE LEVELS TABLE
def populate_unit_size_levels_table():
    res = execute(POPULATE_UNIT_SIZE_LEVELS_TABLE)
    
    if res:
        return{ "message" : "Table populated!" }, 200
    else:
        return{ "message" : "Could not populate table" }, 404
 
#CLEAR SIZE LEVELS TABLE
def clear_unit_size_levels_table():
    res = execute(CLEAR_UNIT_SIZE_LEVELS_TABLE)
    
    if res:
        return {"message" : "All rows deleted"}, 200
    else:
        return {"message" : "something went wrong"}, 404 

# CREATE UNIT TRAITS TABLE
def create_unit_traits_table():
    res = execute(CREATE_UNIT_TRAITS_TABLE)
    
    if res:
        return{ "message" : "Table created!"}, 200
    else:
        return{ "message" : "Could not create table" }, 404
    
# POPULATE UNIT TRAITS TABLE
def populate_unit_traits_table():
    res = execute(POPULATE_UNIT_TRAITS_TABLE)
    
    if res:
        return{ "message" : "Table populated!" }, 200
    else:
        return{ "message" : "Could not populate table" }, 404
 

# CREATE UNIT TYPES TABLE
def create_unit_types_table():
    res = execute(CREATE_UNIT_TYPES_TABLE)
    
    if res:
        return{ "message" : "Table created!"}, 200
    else:
        return{ "message" : "Could not create table" }, 404
    
# POPULATE UNIT TYPES TABLE
def populate_unit_types_table():
    res = execute(POPULATE_UNIT_TYPES_TABLE)
    
    if res:
        return{ "message" : "Table populated!" }, 200
    else:
        return{ "message" : "Could not populate table" }, 404
 
from models.Units.Ancestry_trait_relations import CREATE_ANCESTRY_TRAIT_RELATIONS_TABLE, POPULATE_ANCESTRY_TRAIT_RELATIONS_TABLE
from models.Units.Unit_ancestries import CREATE_UNIT_ANCESTRIES_TABLE, POPULATE_UNIT_ANCESTRIES_TABLE
from models.Units.Unit_equipment_levels import CREATE_UNIT_EQUIPMENT_LEVELS_TABLE, POPULATE_UNIT_EQUIPMENT_LEVELS_TABLE
from models.Units.Unit_experience_levels import CREATE_UNIT_EXPERIENCE_LEVELS_TABLE, POPULATE_UNIT_EXPERIENCE_LEVELS_TABLE
from models.Units.Unit_size_levels import CREATE_UNIT_SIZE_LEVELS_TABLE, POPULATE_UNIT_SIZE_LEVELS_TABLE, CLEAR_UNIT_SIZE_LEVELS_TABLE
from models.Units.Unit_traits import CREATE_UNIT_TRAITS_TABLE, POPULATE_UNIT_TRAITS_TABLE
from models.Units.Unit_types import CREATE_UNIT_TYPES_TABLE, POPULATE_UNIT_TYPES_TABLE
from utils.db import execute

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
 
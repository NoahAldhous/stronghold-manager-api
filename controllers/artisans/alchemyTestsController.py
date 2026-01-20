from models.Artisans.Alchemy_tests import CREATE_ALCHEMY_TESTS_TABLE, POPULATE_ALCHEMY_TESTS_TABLE
from utils.db import query, execute

# CREATE ALCHEMY TESTS TABLE
def create_alchemy_tests_table():
    res = execute(CREATE_ALCHEMY_TESTS_TABLE)
    
    if res:
        return { "message" : "table created" }, 200
    else: 
        return { "message" : "error, could not create table" }, 404

# POPULARE ALCHEMY TESTS TABLE    
def populate_alchemy_tests_table():
    res = execute(POPULATE_ALCHEMY_TESTS_TABLE)
    
    if res:
        return { "message" : "table populated" }, 200
    else: 
        return { "message" : "error, could not populate table" }, 404
from models.Class_feature_improvments import CREATE_CLASS_FEATURE_RESTRICTIONS_TABLE, CREATE_CLASS_FEATURE_IMPROVEMENTS_TABLE, POPULATE_CLASS_FEATURE_RESTRICTIONS_TABLE, POPULATE_CLASS_FEATURE_IMPROVEMENTS_TABLE, GET_ALL_CLASS_FEATURE_IMPROVEMENTS, GET_CLASS_FEATURE_IMPROVEMENT_BY_CLASS_ID, CLEAR_CLASS_FEATURE_RESTRICTIONS_TABLE, CLEAR_CLASS_FEATURE_IMPROVEMENTS_TABLE
from utils.db import query, execute

# CREATE RESTRICTIONS TABLE
def create_class_feature_restrictions_table():
    res = execute(CREATE_CLASS_FEATURE_RESTRICTIONS_TABLE)
    
    if res:
        return{ "message" : "Table created successfully!"}, 200
    else:
        return{ "message" : "Could not create table"}, 404

# CREATE IMPROVEMENTS TABLE
def create_class_feature_improvements_table():
    res = execute(CREATE_CLASS_FEATURE_IMPROVEMENTS_TABLE)
    
    if res:
        return{ "message" : "Table created successfully!"}, 200
    else:
        return{ "message" : "Could not create table"}, 404

# POPULATE RESTRICTIONS TABLE
def populate_class_feature_restrictions_table():
    res = execute(POPULATE_CLASS_FEATURE_RESTRICTIONS_TABLE)
    
    if res:
        return{ "message" : "Table populated successfully!"}, 200
    else:
        return{ "message" : "Could not populate table"}, 404

# POPULATE IMPROVEMENTS TABLE
def populate_class_feature_improvements_table():
    res = execute(POPULATE_CLASS_FEATURE_IMPROVEMENTS_TABLE)
    
    if res:
        return{ "message" : "Table populated successfully!"}, 200
    else:
        return{ "message" : "Could not populate table"}, 404

# GET ALL IMPROVEMENTS
def get_all_class_feature_improvements():
    data = query(GET_ALL_CLASS_FEATURE_IMPROVEMENTS, fetchone=False)
    
    if data:
        return{ "message" : "Success!", "data" : data}, 200
    else:
        return{ "message" : "Could not fetch data" }, 404

# GET IMPROVEMENT BY CLASS ID
def get_class_feature_improvement_by_class_id(class_id):
    data = query(GET_CLASS_FEATURE_IMPROVEMENT_BY_CLASS_ID, (class_id,), fetchone=True)
    
    if data:
        return{ "message" : "Success!", "data" : data}, 200
    else:
        return{ "message" : "Could not fetch data" }, 404

# CLEAR RESTRICTIONS TABLE
def clear_class_feature_restrictions_table():
    res = execute(CLEAR_CLASS_FEATURE_RESTRICTIONS_TABLE)
    
    if res:
        return{ "message" : "All rows deleted" }, 200
    else:
        return{ "message" : "Something went wrong"}, 404

# CLEAR IMPROVEMENTS TABLE
def clear_class_feature_improvements_table():
    res = execute(CLEAR_CLASS_FEATURE_IMPROVEMENTS_TABLE)
    
    if res:
        return{ "message" : "All rows deleted" }, 200
    else:
        return{ "message" : "Something went wrong"}, 404

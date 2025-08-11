from models.Stronghold_type_features import CREATE_STRONGHOLD_TYPE_FEATURES_TABLE, INSERT_STRONGHOLD_TYPE_FEATURES, ADD_NEW_STRONGHOLD_TYPE_FEATURE, GET_ALL_STRONGHOLD_TYPE_FEATURES, GET_STRONGHOLD_TYPE_FEATURE_BY_ID, UPDATE_STRONGHOLD_TYPE_FEATURE_BY_ID, DELETE_STRONGHOLD_TYPE_FEATURE_BY_ID
from utils.db import query, execute
from flask import request

# CREATE STRONGHOLD TYPE FEATURES TABLE
def create_stronghold_type_features_table():
    res = execute(CREATE_STRONGHOLD_TYPE_FEATURES_TABLE)
    
    if res:
        return{"message" : "Table created"}, 200
    else:
        return{"message" : "Oops, an error occured"}, 404

# POPULATE STRONGHOLD TYPE FEATURES TABLE
def populate_stronghold_type_features_table():
    execute(CREATE_STRONGHOLD_TYPE_FEATURES_TABLE)
    res = execute(INSERT_STRONGHOLD_TYPE_FEATURES)
    
    if res:
        return{"message" : "Table populated!"}, 200
    else:
        return{"message" : "Oops, an error occured"}, 404

# ADD NEW STRONGHOLD TYPE FEATURE
def add_new_stronghold_type_feature():
    data = request.get_json()
    strongholdType = data["stronghold_type"]
    featureName = data["feature_name"]
    featureDecription = data["feature_description"]
    res = execute(ADD_NEW_STRONGHOLD_TYPE_FEATURE, (strongholdType, featureName, featureDecription))
    
    if res: 
        return {"message" : "new feature added successfully!"}, 201
    else: return {"message" : "could not add feature"}, 404

# GET ALL STRONGHOLD TYPE FEATURES
def get_all_stronghold_type_features():
    data = query(GET_ALL_STRONGHOLD_TYPE_FEATURES, fetchone = False)
    
    if data:
            return{"message" : "Success!", "data" : data}, 200
    else:
        return{"message" : "Could not fetch data"}, 404
    
# GET STRONGHOLD TYPE FEATURE BY ID
def get_stronghold_type_feature_by_id(id):
    data = query(GET_STRONGHOLD_TYPE_FEATURE_BY_ID, (id,), fetchone = True)

    if data:
            return{"message" : "Success!", "data" : data}, 200
    else:
        return{"message" : "Could not fetch data"}, 404
    
# UPDATE STRONGHOLD TYPE FEATURE BY ID
def update_stronghold_type_feature_by_id(id):
    data = request.get_json()
    newFeatureName = data["name"]
    newFeatureDescription = data["description"]
    res = execute(UPDATE_STRONGHOLD_TYPE_FEATURE_BY_ID, (id, newFeatureName, newFeatureDescription,))
    
    if res:
        return {"message" : "Item updated successfully"}, 200
    else:
        return {"message" : "Could not find item"}, 404

# DELETE STRONGHOLD TYPE FEATURE BY ID
def delete_stronghold_type_feature_by_id(id):
    res = execute(DELETE_STRONGHOLD_TYPE_FEATURE_BY_ID, (id,))
    
    if res:
        return {"message" : "Item deleted successfuly"}, 200
    else:
        return {"message" : "Could not find item"}, 404
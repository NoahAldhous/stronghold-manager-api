from models.Stronghold_type_stats import GET_ALL_STRONGHOLD_STATS, GET_STRONGHOLD_STATS_BY_TYPE_AND_LEVEL
from utils.db import query

# GET STATS BY TYPE ID
# def get_stronghold_type_stats_by_type_id(typeId):
#     data = query(GET_STATS_BY_TYPE, (typeId,) fetchone=False)
    
#     if data:
#         return {"message" : "Success!", "data": data}, 201
#     else:
#         return {"message" : "Something went wrong"}, 404

def get_all_stronghold_type_stats():
    data = query(GET_ALL_STRONGHOLD_STATS, fetchone=False)
    
    if data:
        return {"message" : "Success!", "data": data}, 201
    else:
        return {"message" : "Something went wrong"}, 404
    
def get_stronghold_stats_by_type_and_level(type,level):
    data = query(GET_STRONGHOLD_STATS_BY_TYPE_AND_LEVEL, (type,level,), fetchone=True)
    
    if data:
        return {"message" : "Success!", "data": data}, 201
    else:
        return {"message" : "Something went wrong"}, 404
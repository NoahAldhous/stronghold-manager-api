from models.Stronghold_treasury import UPDATE_TREASURY_CURRENCY
from utils.db import query, execute
from flask import request

# UPDATE STRONGHOLD TREASURY CURRENCY
def update_stronghold_treasury_currency(stronghold_id):
    data = request.get_json()
    platinum = data["pp"]
    gold = data["gp"]
    silver = data["sp"]
    electrum = data["ep"]
    copper = data["cp"]
    
    res = execute(UPDATE_TREASURY_CURRENCY, (platinum, gold, silver, electrum, copper, stronghold_id))
    
    if res:
        return{"message" : "Treasury Updated"}, 200
    else:
        return{"message" : "Oops, an error occured"}, 404
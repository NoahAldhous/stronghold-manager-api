from db import query, execute
from models.Users import GET_ALL_USERS

if __name__ == "main":
    result= query(GET_ALL_USERS)
    print(result)

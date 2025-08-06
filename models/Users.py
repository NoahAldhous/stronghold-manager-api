CREATE_USERS_TABLE = (
    "CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, user_name TEXT, email TEXT UNIQUE, user_password TEXT, account_created DATE);"
)

GET_ALL_USERS = "SELECT * FROM users;"
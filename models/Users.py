CREATE_USERS_TABLE = (
    "CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, user_name TEXT, email TEXT UNIQUE, user_password TEXT, account_created DATE);"
)

GET_ALL_USERS = (
    "SELECT * FROM users;"
)

INSERT_USER_RETURN_ID = (
    "INSERT INTO users (user_name, email, user_password, account_created) VALUES (%s, %s, %s, %s) RETURNING id;"
)

GET_USER_BY_ID = (
    "SELECT * FROM users WHERE id = %s;"
)
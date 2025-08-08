CREATE_USERS_TABLE = (
    "CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, user_name TEXT, email TEXT UNIQUE, user_password TEXT, account_created DATE);"
)

INSERT_USER_RETURN_ID = (
    "INSERT INTO users (user_name, email, user_password, account_created) VALUES (%s, %s, %s, %s) RETURNING id;"
)

GET_ALL_USERS = (
    "SELECT * FROM users;"
)

GET_USER_BY_ID = (
    "SELECT * FROM users WHERE id = %s;"
)

UPDATE_USER_PASSWORD_BY_ID = (
    "UPDATE users SET user_password = %s WHERE id = %s"
)

UPDATE_USER_NAME_BY_ID = (
    "UPDATE users SET user_name = %s WHERE id = %s"
)

DELETE_USER_BY_ID = (
    "DELETE FROM users WHERE id = %s;"
)
CREATE_USERS_TABLE = (
    """CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY, 
        user_name TEXT UNIQUE NOT NULL, 
        email TEXT UNIQUE NOT NULL, 
        password_hash TEXT NOT NULL,
        role TEXT NOT NULL DEFAULT 'user',
        created_at TIMESTAMPTZ DEFAULT now()
        is_active BOOLEAN DEFAULT TRUE
    );"""
)

INSERT_USER = (
    """INSERT INTO 
        users (
            user_name, 
            email, 
            password_hash
        ) 
        VALUES (%s, %s, %s) 
        RETURNING 
            id, 
            user_name, 
            email, 
            role
    ;"""
)

GET_ALL_USERS = (
    "SELECT * FROM users;"
)

GET_USER_BY_ID = (
    "SELECT * FROM users WHERE id = %s;"
)

GET_USER_BY_EMAIL = (
    "SELECT id, email, role, password_hash FROM users WHERE email = %s;"
)

UPDATE_USER_PASSWORD_BY_ID = (
    "UPDATE users SET user_password = %s WHERE id = %s;"
)

UPDATE_USER_NAME_BY_ID = (
    "UPDATE users SET user_name = %s WHERE id = %s;"
)

DELETE_USER_BY_ID = (
    "DELETE FROM users WHERE id = %s;"
)

DELETE_USERS_TABLE = (
    "DROP TABLE users;"
)
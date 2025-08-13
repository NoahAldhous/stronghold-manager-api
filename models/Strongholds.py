CREATE_STRONGHOLDS_TABLE = (
    "CREATE TABLE IF NOT EXISTS strongholds (id SERIAL PRIMARY KEY, user_id INT, FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE, stronghold_name TEXT, owner_name TEXT, stronghold_level INTEGER, stronghold_type_id INT, FOREIGN KEY(stronghold_type_id) REFERENCES stronghold_types(id), created_at TIMESTAMP);"
)

INSERT_STRONGHOLD_RETURN_ID = (    
    "INSERT INTO strongholds (user_id, stronghold_name, owner_name, stronghold_level, stronghold_type_id, created_at) VALUES (%s, %s, %s, %s, (SELECT id FROM stronghold_types WHERE type_name = %s), %s) RETURNING id;"
)

GET_STRONGHOLDS_BY_USER_ID = (
    "SELECT id, stronghold_name, owner_name, stronghold_level, stronghold_type_id FROM strongholds WHERE user_id = %s;"
)

GET_STRONGHOLD_BY_ID = (
    "SELECT * FROM strongholds WHERE id = %s;"
)

GET_STRONGHOLD_BY_ID_RETURN_ALL_STRONGHOLD_DATA = (
    """SELECT
        s.id,
        s.stronghold_name,
        s.owner_name,
        s.stronghold_level,
        (SELECT type_name AS stronghold_type from stronghold_types WHERE id = s.stronghold_type_id)
        FROM strongholds s;
    """
)

DELETE_STRONGHOLDS_TABLE = (
    "DROP TABLE strongholds;"
)
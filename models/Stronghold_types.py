CREATE_STRONGHOLD_TYPES_TABLE = (
    "CREATE TABLE IF NOT EXISTS stronghold_types (id SERIAL PRIMARY KEY, type_name TEXT UNIQUE);"
)

INSERT_STRONGHOLD_TYPES = (
    "INSERT INTO stronghold_types (type_name) VALUES ('keep'),('tower'),('temple'),('establishment'),('castle') RETURNING *;"
)

GET_ALL_STRONGHOLD_TYPES = (
    "SELECT * FROM stronghold_types;"
)

UPDATE_STRONGHOLD_TYPE_BY_ID = (
    "UPDATE stronghold_types SET type_name = %s WHERE id = %s;"
)

DELETE_STRONGHOLD_TYPE_BY_ID = (
    "DELETE FROM stronghold_types WHERE ID = %s;"
)

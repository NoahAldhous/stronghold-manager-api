CREATE_STRONGHOLD_SIZE_LEVELS_TABLE = (
    "CREATE TABLE IF NOT EXISTS stronghold_size_levels (id SERIAL PRIMARY KEY, stronghold_level INTEGER, stronghold_type_id INT, FOREIGN KEY(stronghold_type_id) REFERENCES stronghold_types(id), stronghold_size INTEGER);"
)

INSERT_STRONGHOLD_SIZE_LEVEL = (
    "INSERT INTO stronghold_size_levels (stronghold_level, stronghold_type_id, stronghold_size) VALUES (%s, (SELECT id FROM stronghold_types WHERE type_name = %s), %s);"
)

GET_ALL_STRONGHOLD_SIZE_LEVELS = (
    "SELECT * FROM stronghold_size_levels;"
)

GET_STRONGHOLD_SIZE_LEVEL_BY_TYPE_ID = (
    "SELECT * FROM stronghold_size_levels WHERE stronghold_type_id = %s;"
)

GET_STRONGHOLD_SIZE_BY_LEVEL = (
    "SELECT * FROM stronghold_size_levels WHERE stronghold_level = %s;"
)

UPDATE_STRONGHOLD_SIZE_LEVEL_BY_ID = (
    "UPDATE stronghold_size_levels SET stronghold_size = %s WHERE id = %s;"
)

DELETE_STRONGHOLD_SIZE_LEVEL_BY_ID = (
    "DELETE FROM stronghold_size_levels WHERE id = %s;"
)
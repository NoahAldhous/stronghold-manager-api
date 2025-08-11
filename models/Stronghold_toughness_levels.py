CREATE_STRONGHOLD_TOUGHNESS_LEVELS_TABLE = (
    "CREATE TABLE IF NOT EXISTS stronghold_toughness_levels (id SERIAL PRIMARY KEY, stronghold_level INT, stronghold_type_id INT, toughness INT, FOREIGN KEY(stronghold_type_id) REFERENCES stronghold_types(id));"
)

INSERT_STRONGHOLD_TOUGHNESS_LEVEL = (
    "INSERT INTO stronghold_toughness_levels (stronghold_level, stronghold_type_id, toughness) VALUES (%s, (SELECT id FROM stronghold_types WHERE type_name = %s), %s);"
)

GET_ALL_STRONGHOLD_TOUGHNESS_LEVELS = (
    "SELECT * FROM stronghold_toughness_levels;"
)

GET_STRONGHOLD_TOUGHNESS_LEVELS_BY_TYPE_ID = (
    "SELECT * FROM stronghold_toughness_levels WHERE stronghold_type_id = %s;"
)

GET_STRONGHOLD_TOUGHNESS_BY_LEVEL = (
    "SELECT * FROM stronghold_toughness_levels WHERE stronghold_level = %s;"
)

UPDATE_STRONGHOLD_TOUGHNESS_LEVEL_BY_ID = (
    "UPDATE stronghold_toughness_levels SET toughness = %s WHERE id = %s;"
)

DELETE_STRONGHOLD_TOUGHNESS_LEVEL_BY_ID = (
    "DELETE FROM stronghold_toughness_levels WHERE id = %s;"
)

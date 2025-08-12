CREATE_STRONGHOLD_CONSTRUCTION_LEVELS_TABLE = (
    "CREATE TABLE IF NOT EXISTS stronghold_construction_levels (id SERIAL PRIMARY KEY, stronghold_level INT, stronghold_type_id INT, cost_to_build INTEGER, time_to_build INTEGER, fortification_morale_bonus INTEGER, FOREIGN KEY(stronghold_type_id) REFERENCES stronghold_types(id));"
)

INSERT_STRONGHOLD_CONSTRUCTION_LEVEL = (
    "INSERT INTO stronghold_construction_levels (stronghold_level, stronghold_type_id, cost_to_build, time_to_build, fortification_morale_bonus) VALUES (%s, (SELECT id FROM stronghold_types WHERE type_name = %s), %s, %s, %s);"
)

GET_ALL_STRONGHOLD_CONSTRUCTION_LEVELS = (
    "SELECT * FROM stronghold_construction_levels;"
)

GET_STRONGHOLD_CONSTRUCTION_LEVELS_BY_TYPE_ID = (
    "SELECT * FROM stronghold_construction_levels WHERE stronghold_type_id = %s;"
)

GET_STRONGHOLD_CONSTRUCTION_BY_LEVEL = (
    "SELECT * FROM stronghold_construction_levels WHERE stronghold_level = %s;"
)

UPDATE_STRONGHOLD_CONSTRUCTION_LEVEL_BY_ID = (
    "UPDATE stronghold_construction_levels SET cost_to_build = %s, time_to_build = %s, fortification_morale_bonus = %s WHERE id = %s;"
)

DELETE_STRONGHOLD_CONSTRUCTION_LEVEL_BY_ID = (
    "DELETE FROM stronghold_construction_levels WHERE id = %s;"
)
CREATE_STRONGHOLD_TOUGHNESS_LEVELS_TABLE = (
    "CREATE TABLE IF NOT EXISTS stronghold_toughness_levels (id SERIAL PRIMARY KEY, stronghold_level INT, stronghold_type_id INT, toughness INT, FOREIGN KEY(stronghold_type_id) REFERENCES stronghold_types(id));"
)

INSERT_STRONGHOLD_TOUGHNESS_LEVEL = (
    "INSERT INTO stronghold_toughness_levels (stronghold_level, stronghold_type_id, toughness) VALUES (%s, (SELECT id FROM stronghold_types WHERE type_name = %s), %s);"
)

POPULATE_STRONGHOLD_TOUGHNESS_LEVELS_TABLE = (
    """INSERT INTO stronghold_toughness_levels (
        stronghold_level,
        stronghold_type_id,
        stronghold_toughness
    ) SELECT 
        level.level,
        types.id,
        levels.toughness
    FROM (
        VALUES
            (
                1, 'keep', 22
            ),
            (
                2, 'keep', 24
            ),
            (
                3, 'keep', 26
            ),
            (
                4, 'keep', 28
            ),
            (
                5, 'keep', 30
            ),
            (
                1, 'tower', 18
            ),
            (
                2, 'tower', 20
            ),
            (
                3, 'tower', 22
            ),
            (
                4, 'tower', 24
            ),
            (
                5, 'tower', 26
            ),
            (
                1, 'temple', 18
            ),
            (
                2, 'temple', 20
            ),
            (
                3, 'temple', 22
            ),
            (
                4, 'temple', 24
            ),
            (
                5, 'temple', 26
            ),
            (
                1, 'establishment', 0
            ),
            (
                2, 'establishment', 0
            ),
            (
                3, 'establishment', 0
            ),
            (
                4, 'establishment', 0
            ),
            (
                5, 'establishment', 0
            ),
    ) AS level(level, type_name, toughness)
    JOIN stronghold_types AS types
        ON types.type_name = level.type_name
    """
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

CLEAR_STRONGHOLD_TOUGHNESS_LEVELS_TABLE = (
    "DELETE FROM stronghold_toughness_levels;"
)

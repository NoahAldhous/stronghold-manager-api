CREATE_STRONGHOLD_SIZE_LEVELS_TABLE = (
    "CREATE TABLE IF NOT EXISTS stronghold_size_levels (id SERIAL PRIMARY KEY, stronghold_level INTEGER, stronghold_type_id INT, FOREIGN KEY(stronghold_type_id) REFERENCES stronghold_types(id), stronghold_size INTEGER);"
)

INSERT_STRONGHOLD_SIZE_LEVEL = (
    "INSERT INTO stronghold_size_levels (stronghold_level, stronghold_type_id, stronghold_size) VALUES (%s, (SELECT id FROM stronghold_types WHERE type_name = %s), %s);"
)

POPULATE_STRONGHOLD_SIZE_LEVELS_TABLE = (
    """INSERT INTO stronghold_size_levels (
        stronghold_level,
        stronghold_type_id,
        stronghold_size
    ) SELECT
        levels.level,
        types.id,
        levels.size
    FROM (
        VALUES
            (
                1, 'keep', 6    
                2, 'keep', 8    
                3, 'keep', 10    
                4, 'keep', 12   
                5, 'keep', 20   
                1, 'tower', 4    
                2, 'tower', 6    
                3, 'tower', 8    
                4, 'tower', 10   
                5, 'tower', 12   
                1, 'temple', 4    
                2, 'temple', 6    
                3, 'temple', 8    
                4, 'temple', 10   
                5, 'temple', 12   
                1, 'establishment', 0    
                2, 'establishment', 0    
                3, 'establishment', 0    
                4, 'establishment', 0   
                5, 'establishment', 0   
            ),
    )
    """
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

CLEAR_STRONGHOLD_SIZE_LEVELS_TABLE = (
    "DELETE FROM stronghold_size_levels;"
)
CREATE_UNIT_SIZE_LEVELS_TABLE = (
    """CREATE TABLE IF NOT EXISTS unit_size_levels (
        id SERIAL PRIMARY KEY,
        level_name INT UNIQUE NOT NULL,
        unit_size INT UNIQUE NOT NULL,
        cost_modifier NUMERIC UNIQUE NOT NULL    
    );"""
)

POPULATE_UNIT_SIZE_LEVELS_TABLE = (
    """INSERT INTO unit_size_levels (
        level_name,
        unit_size,
        cost_modifier
    ) SELECT
        levels.name,
        levels.size,
        levels.modifier
    FROM (
        VALUES
            (
                1,
                4,
                0.66
            ),
            (
                2,
                6,
                1
            ),
            (
                3,
                8,
                1.33
            ),
            (
                4,
                10,
                1.66
            ),
            (
                5,
                12,
                2
            )
    ) AS levels(name, size, modifier);
    """
)

CLEAR_UNIT_SIZE_LEVELS_TABLE = (
    "DELETE FROM unit_size_levels;"
)

GET_ALL_UNIT_SIZES = (
    """SELECT
        id,
        level_name AS "levelName",
        unit_size AS "size",
        cost_modifier AS "costModifier" 
    FROM unit_size_levels;"""
)
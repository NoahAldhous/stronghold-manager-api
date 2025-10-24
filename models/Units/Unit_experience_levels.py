CREATE_UNIT_EXPERIENCE_LEVELS_TABLE = (
    """CREATE TABLE IF NOT EXISTS unit_experience_levels (
        id SERIAL PRIMARY KEY,
        level_name TEXT UNIQUE NOT NULL,
        attack_bonus INT,
        toughness_bonus INT,
        morale_bonus INT
    );"""
)

POPULATE_UNIT_EXPERIENCE_LEVELS_TABLE = (
    """INSERT INTO unit_experience_levels (
        level_name,
        attack_bonus,
        toughness_bonus,
        morale_bonus    
    ) SELECT 
        levels.name,
        levels.attack,
        levels.toughness,
        levels.morale
    FROM (
        VALUES
            (
                'green',
                0,
                0,
                0
            ),
            (
                'regular',
                1,
                1,
                1
            ),
            (
                'seasoned',
                1,
                1,
                2
            ),
            (
                'veteran',
                1,
                1,
                3
            ),
            (
                'elite',
                2,
                2,
                4
            ),
            (
                'super-elite',
                2,
                2,
                5
            )
    ) AS levels(name, attack, toughness, morale);
    """
)

GET_ALL_UNIT_EXPERIENCE_LEVELS = (
    """SELECT 
        id,
        level_name AS "levelName",
        attack_bonus AS "attackBonus",
        toughness_bonus AS "toughnessBonus",
        morale_bonus AS "moraleBonus"
    FROM unit_experience_levels;"""
)
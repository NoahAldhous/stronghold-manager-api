CREATE_UNIT_EQUIPMENT_LEVELS_TABLE = (
    """CREATE TABLE IF NOT EXISTS unit_equipment_levels (
        id SERIAL PRIMARY KEY,
        level_name TEXT UNIQUE NOT NULL,
        power_bonus INT,
        defense_bonus INT
    );"""
)

POPULATE_UNIT_EQUIPMENT_LEVELS_TABLE = (
    """INSERT INTO unit_equipment_levels (
        level_name,
        power_bonus,
        defense_bonus
    ) SELECT
        levels.name,
        levels.power,
        levels.defense
    FROM (
        VALUES
            (
                'light',
                1,
                1
            ),
            (
                'medium',
                2,
                2
            ),
            (
                'heavy',
                4,
                4
            ),
            (
                'super-heavy',
                6,
                6
            )
    ) AS levels(name, power, defense);
    """
)

GET_ALL_UNIT_EQUIPMENT_LEVELS = (
    """SELECT 
        id,
        level_name AS "levelName",
        power_bonus AS "powerBonus",
        defense_bonus AS "defenseBonus"
    FROM unit_equipment_levels;"""
)
CREATE_UNIT_TYPES_TABLE = (
    """CREATE TABLE IF NOT EXISTS unit_types (
        id SERIAL PRIMARY KEY,
        type_name TEXT UNIQUE NOT NULL,
        attack_bonus INT,
        power_bonus INT, 
        defense_bonus INT,
        toughness_bonus INT,
        morale_bonus INT,
        cost_modifier NUMERIC    
    );"""
)

POPULATE_UNIT_TYPES_TABLE = (
    """INSERT INTO unit_types (
        type_name,
        attack_bonus,
        power_bonus,
        defense_bonus,
        toughness_bonus,
        morale_bonus,
        cost_modifier    
    ) SELECT 
        types.name,
        types.attack,
        types.power,
        types.defense,
        types.toughness,
        types.morale,
        types.cost
    FROM (
        VALUES
            (
                'flying',
                0,
                0,
                0,
                0,
                3,
                2
            ),
            (
                'archers',
                0,
                1,
                0,
                0,
                1,
                1.75
            ),
            (
                'cavalry',
                1,
                1,
                0,
                0,
                2,
                1.5
            ),
            (
                'levies',
                0,
                0,
                0,
                0,
                -1,
                0.75
            ),
            (
                'infantry',
                0,
                0,
                1,
                1,
                0,
                1
            ),
            (
                'siege engine',
                1,
                1,
                0,
                1,
                0,
                1.5
            )
    ) AS types(name, attack, power, defense, toughness, morale, cost);
    """
)
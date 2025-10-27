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

GET_ALL_UNIT_TYPES = (
    """SELECT 
        t.id,
        t.type_name AS "name",
        t.attack_bonus AS "attackBonus",
        t.power_bonus "powerBonus", 
        t.defense_bonus AS "defenseBonus",
        t.toughness_bonus AS "toughnessBonus",
        t.morale_bonus AS "moraleBonus",
        t.cost_modifier As "costModifier",
        COALESCE(
            (
                SELECT json_agg(
                    json_build_object(
                        'traitName', st.trait_name,
                        'traitDescription', st.trait_description,
                        'cost', st.cost
                    )
                )
                FROM unit_traits st
                WHERE 
                    (t.type_name = 'cavalry' AND st.trait_name = 'charge')
                OR 
                    (t.type_name = 'levies' AND st.trait_name = 'always diminished')
            ),
            '[]'
        )::jsonb AS traits
    FROM unit_types t
    GROUP BY 
    t.id,
    t.type_name,
    t.attack_bonus,
    t.power_bonus, 
    t.defense_bonus,
    t.toughness_bonus,
    t.morale_bonus,
    t.cost_modifier
    ;"""
)
CREATE_UNIT_ANCESTRIES_TABLE = (
    """CREATE TABLE IF NOT EXISTS unit_ancestries (
        id SERIAL PRIMARY KEY,
        ancestry_name TEXT UNIQUE NOT NULL,
        attack_bonus INT,
        power_bonus INT,
        defense_bonus INT,
        toughness_bonus INT,
        morale_bonus INT
    )
    """
)

POPULATE_UNIT_ANCESTRIES_TABLE = (
    """INSERT INTO unit_ancestries (
        ancestry_name,
        attack_bonus,
        power_bonus,
        defense_bonus,
        toughness_bonus,
        morale_bonus
    ) SELECT
        ancestries.name,
        ancestries.attack,
        ancestries.power,
        ancestries.defense,
        ancestries.toughness,
        ancestries.morale
    FROM (
        VALUES 
            (
                'bugbear',
                2,
                0,
                0,
                0,
                1
            ),
            (
                'dragonborn',
                2,
                2,
                1,
                1,
                1
            ),
            (
                'dwarf',
                3,
                1,
                1,
                1,
                2
            ),
            (
                'elf',
                2,
                0,
                0,
                0,
                1
            ),
            (
                'elf (winged)',
                1,
                1,
                0,
                0,
                1
            ),
            (
                'ghoul',
                -1,
                0,
                2,
                2,
                0
            ),
            (
                'gnoll',
                2,
                0,
                0,
                0,
                1
            ),
            (
                'gnome',
                1,
                -1,
                1,
                -1,
                1
            ),
            (
                'goblin',
                -1,
                -1,
                1,
                -1,
                0
            ),
            (
                'hobgoblin',
                2,
                0,
                0,
                0,
                1
            ),
            (
                'human',
                2,
                0,
                0,
                0,
                1
            ),
            (
                'kobold',
                -1,
                -1,
                1,
                -1,
                -1
            ),
            (
                'lizardfolk',
                2,
                1,
                -1,
                1,
                1
            ),
            (
                'ogre',
                0,
                2,
                0,
                2,
                1
            ),
            (
                'orc',
                2,
                1,
                1,
                1,
                2
            ),
            (
                'skeleton',
                -2,
                -1,
                1,
                1,
                1
            ),
            (
                'treant',
                0,
                2,
                0,
                2,
                0
            ),
            (
                'troll',
                0,
                2,
                0,
                2,
                0
            ),
            (
                'zombie',
                -2,
                0,
                2,
                2,
                2
            )       
    ) AS ancestries(name, attack, power, defense, toughness, morale);
    """
)

GET_ALL_UNIT_ANCESTRIES = (
    """SELECT 
        a.ancestry_name AS "name",
        a.attack_bonus AS "attackBonus",
        a.power_bonus AS "powerBonus",
        a.defense_bonus AS "defenseBonus",
        a.toughness_bonus AS "toughnessBonus",
        a.morale_bonus AS "moraleBonus",
        COALESCE(
            json_agg(
                json_build_object(
                    'traitName', tr.trait_name,
                    'traitDescription', tr.trait_description,
                    'cost', tr.cost
                )
            ) FILTER (WHERE tr.id IS NOT NULL),
            '[]'
        ) AS traits
        FROM unit_ancestries a
        LEFT JOIN ancestry_trait_relations r
            ON r.ancestry_id = a.id
        LEFT JOIN unit_traits tr
            ON tr.id = r.trait_id
        GROUP BY 
            a.ancestry_name,
            a.attack_bonus,
            a.power_bonus,
            a.defense_bonus,
            a.toughness_bonus,
            a.morale_bonus;
    """
)
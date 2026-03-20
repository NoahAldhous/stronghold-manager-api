CREATE_RETAINERS_TABLE = (
    """CREATE TABLE IF NOT EXISTS retainers (
        id SERIAL PRIMARY KEY,
        class_id INT NOT NULL REFERENCES classes(id) ON DELETE CASCADE,
        retainer_name TEXT UNIQUE NOT NULL,
        armour_id INT NOT NULL REFERENCES retainer_armour_classes(id)
        );"""
)

POPULATE_RETAINERS_TABLE = (
    """INSERT INTO retainers (
        class_id,
        retainer_name,
        armour_id    
    ) SELECT 
        classes.id,
        retainers.name,
        armour.id
    FROM (
        VALUES
            (
                'barbarian',
                'reaver',
                'medium'
            ),
            (
                'barbarian',
                'spirit warden',
                'medium'
            ),
            (
                'bard',
                'loremaster',
                'light'
            ),
            (
                'bard',
                'troubadour-warrior',
                'light'
            ),
            (
                'cleric',
                'curate',
                'medium'
            ),
            (
                'cleric',
                'exorcist',
                'medium'
            ),
            (
                'cleric',
                'healer',
                'heavy'
            ),
            (
                'cleric',
                'shadow priest',
                'medium'
            ),
            (
                'cleric',
                'stormspeaker',
                'heavy'
            ),
            (
                'cleric',
                'warden',
                'medium'
            ),
            (
                'cleric',
                'battle priest',
                'heavy'
            ),
            (
                'druid',
                'mystic',
                'medium'
            ),
            (
                'druid',
                'skinwalker',
                'medium'
            ),
            (
                'fighter',
                'knight-sorcerer',
                'heavy'
            ),
            (
                'fighter',
                'swordmaster',
                'heavy'
            ),
            (
                'fighter',
                'warlord',
                'heavy'
            ),
            (
                'monk',
                'acolyte of the way',
                'medium'
            ),
            (
                'monk',
                'acolyte of darkness',
                'medium'
            ),
            (
                'monk',
                'elemental acolyte',
                'medium'
            ),
            (
                'paladin',
                'cavalier',
                'heavy'
            ),
            (
                'paladin',
                'justicar',
                'heavy'
            ),
            (
                'paladin',
                'knight of the green order',
                'heavy'
            ),
            (
                'ranger',
                'beast lord',
                'medium'
            ),
            (
                'ranger',
                'tracker',
                'medium'
            ),
            (
                'rogue',
                'executioner',
                'light'
            ),
            (
                'rogue',
                'guild adept',
                'light'
            ),
            (
                'rogue',
                'cutpurse',
                'light'
            ),
            (
                'sorcerer',
                'thaumaturgist',
                'light'
            ),
            (
                'sorcerer',
                'chaos mage',
                'light'
            ),
            (
                'warlock',
                'alienist',
                'light'
            ),
            (
                'warlock',
                'diabolist',
                'light'
            ),
            (
                'warlock',
                'exarch',
                'light'
            ),
            (
                'wizard',
                'conjurer',
                'light'
            ),
            (
                'wizard',
                'enchanter',
                'light'
            ),
            (
                'wizard',
                'evoker',
                'light'
            ),
            (
                'wizard',
                'illusionist',
                'light'
            ),
            (
                'wizard',
                'necromancer',
                'light'
            ),
            (
                'wizard',
                'seer',
                'light'
            ),
            (
                'wizard',
                'shaper',
                'light'
            ),
            (
                'wizard',
                'theurgist',
                'light'
            )   
    ) AS retainers(class, name, armour)
        JOIN retainer_armour_classes AS armour
            ON retainers.armour = armour.armour_type
        JOIN classes
            ON retainers.class = classes.class_name
    ;"""
)

GET_ALL_RETAINERS = (
    """SELECT 
        r.id AS "id",
        r.retainer_name AS "name",
        c.class_name AS "class",
        json_agg( DISTINCT
            jsonb_build_object(
                'name', pa.ability_name,
                'abbreviation', pa.abbreviation
            ) 
        ) AS "primaryAbility",
        json_agg( DISTINCT
            jsonb_build_object(
                'name', sa.ability_name,
                'abbreviation', sa.abbreviation
            )
        ) AS "savingThrows",
        json_build_object(
            'type', ac.armour_type,
            'value', ac.armour_class
        ) AS "armourClass",
            json_build_object(
                'name', s.ability_name,
                'type', s.ability_type,
                'hitOrDC', s.hit_dc,
                'damage', json_build_object(
                    'average', s.average_damage,
                    'numberOfDice', s.dice_quantity,
                    'diceSize', s.dice_size,
                    'modifier', s.damage_modifier,
                    'type', s.damage_type
                ),
                'range', json_build_object(
                    'type', ar.range_type,
                    'reach', ar.reach,
                    'short', ar.short_range,
                    'long', ar.long_range
                )
            ) AS "signatureAttack"
        FROM retainers r
        LEFT JOIN retainer_armour_classes ac
        ON r.armour_id = ac.id   
        
        LEFT JOIN signature_abilities s
        ON r.id = s.retainer_id
        
        LEFT JOIN signature_ability_ranges ar
        ON ar.id = s.range_id
        
        LEFT JOIN classes c
        ON c.id = r.class_id
        
        LEFT JOIN retainer_class_ability_relations rcar
        ON r.class_id = rcar.class_id
        
        LEFT JOIN abilities pa
        ON rcar.ability_id = pa.id
        
        LEFT JOIN retainer_class_saves_relations rcsr
        ON r.class_id = rcsr.class_id
        
        LEFT JOIN abilities sa
        ON rcsr.save_id = sa.id
        GROUP BY
            r.id,
            c.class_name,
            r.retainer_name,
            ac.armour_type,
            ac.armour_class,
            s.ability_name,
            s.ability_type,
            s.hit_dc,
            s.average_damage,
            s.dice_quantity,
            s.dice_size,
            s.damage_modifier,
            s.damage_type,
            ar.range_type,
            ar.reach,
            ar.short_range,
            ar.long_range
    ;"""
)
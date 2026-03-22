CREATE_STRONGHOLD_RETAINERS_TABLE = (
    """CREATE TABLE IF NOT EXISTS stronghold_retainers (
        id SERIAL PRIMARY KEY,
        individual_name TEXT NOT NULL,
        stronghold_id INT NOT NULL REFERENCES strongholds(id) ON DELETE CASCADE,
        retainer_id INT NOT NULL REFERENCES retainers(id) ON DELETE CASCADE,
        ancestry_id INT NOT NULL REFERENCES retainer_ancestries(id) ON DELETE CASCADE,
        retainer_level INT NOT NULL CHECK (retainer_level BETWEEN 1 AND 20),
        health_levels_lost INT NOT NULL CHECK (health_levels_lost BETWEEN 0 AND retainer_level)
        )"""
)

ADD_STRONGHOLD_RETAINER = (
    """INSERT INTO stronghold_retainers (
        individual_name,
        stronghold_id,
        retainer_id,
        ancestry_id,
        retainer_level,
        health_levels_lost
    ) VALUES (
        %s,
        %s,
        (
            SELECT id
                FROM retainers
                WHERE retainer_name = %s
        ),
        (
            SELECT id
                FROM retainer_ancestries
                WHERE ancestry_name = %s
        ),
        %s,
        %s
    ) RETURNING id;
    """
)

GET_RETAINERS_BY_STRONGHOLD_ID = (
    """SELECT
        sr.id AS "id",
        sr.individual_name AS "name",
        sr.retainer_level AS "level",
        sr.health_levels_lost AS "healthLevelsLost",
        r.retainer_name AS "title",
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
        ) AS "signatureAttack",
        json_build_object(
            'name', ra.ancestry_name,
            'size', ra.ancestry_size,
            'speed', ra.ancestry_speed,
            'darkvision', ra.ancestry_darkvision_distance
        ) AS "ancestry"
        
        FROM stronghold_retainers sr
        LEFT JOIN retainers r
        ON sr.retainer_id = r.id
        
        LEFT JOIN retainer_armour_classes ac
        ON r.armour_id = ac.id   
        
        LEFT JOIN signature_abilities s
        ON sr.retainer_id = s.retainer_id
        
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
        
        LEFT JOIN retainer_ancestries ra
        ON sr.ancestry_id = ra.id
        
        WHERE sr.stronghold_id = %s
        GROUP BY
            sr.id,
            sr.individual_name,
            sr.retainer_level,
            sr.health_levels_lost,
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
            ar.long_range,
            ra.ancestry_name,
            ra.ancestry_size,
            ra.ancestry_speed,
            ra.ancestry_darkvision_distance   
    ;"""
)
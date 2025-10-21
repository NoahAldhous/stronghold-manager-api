CREATE_UNITS_TABLE = (
    """CREATE TABLE IF NOT EXISTS units (
        id SERIAL PRIMARY KEY,
        user_id INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        unit_name TEXT NOT NULL,
        stronghold_id INT REFERENCES strongholds(id) ON DELETE CASCADE,
        ancestry_id INT NOT NULL REFERENCES unit_ancestries(id),
        experience_id INT NOT NULL REFERENCES unit_experience_levels(id),
        equipment_id INT NOT NULL REFERENCES unit_equipment_levels(id),
        type_id INT NOT NULL REFERENCES unit_types(id),
        size_id INT NOT NULL REFERENCES unit_size_levels(id),
        casualties INT NOT NULL DEFAULT 0 CHECK (casualties >= 0),
        mercenary BOOLEAN,
        created_at TIMESTAMP
    );"""
)

ADD_UNIT = (
    """INSERT INTO units (
        user_id,
        unit_name,
        stronghold_id,
        ancestry_id,
        experience_id,
        equipment_id,
        type_id,
        size_id,
        casualties,
        mercenary,
        created_at
    ) VALUES (
        %s,
        %s,
        %s,
        (
            SELECT id
                FROM unit_ancestries
                WHERE ancestry_name = %s
        ),
        (
            SELECT id
                FROM unit_experience_levels
                WHERE level_name = %s
        ),
        (
            SELECT id
                FROM unit_equipment_levels
                WHERE level_name = %s
        ),
        (
            SELECT id 
                FROM unit_types
                WHERE type_name = %s
        ),
        (
            SELECT id
                FROM unit_size_levels
                WHERE level_name = %s
        ),
        %s,
        %s,
        %s
    )
    RETURNING id;
    """
)

GET_UNITS_BY_USER_ID = (
    """SELECT
        u.id AS "unit_id",
        u.unit_name AS "name",
        u.stronghold_id,
        u.user_id,
        u.casualties,
        u.mercenary AS "isMercenary",
        u.created_at AS "creationDate",
        json_build_object(
            'name', a.ancestry_name,
            'attackBonus', a.attack_bonus,
            'powerBonus', a.power_bonus,
            'defenseBonus', a.defense_bonus,
            'toughnessBonus', a.toughness_bonus,
            'moraleBonus', a.morale_bonus
        ) AS ancestry,
        json_build_object(
            'name', x.level_name,
            'attackBonus', x.attack_bonus,
            'toughnessBonus', x.toughness_bonus,
            'moraleBonus', x.morale_bonus
        ) AS experience,
        json_build_object(
            'name', e.level_name,
            'powerBonus', e.power_bonus,
            'defenseBonus', e.defense_bonus
        ) AS equipment,
        json_build_object(
            'name', t.type_name,
            'attackBonus', t.attack_bonus,
            'powerBonus', t.power_bonus,
            'defenseBonus', t.defense_bonus,
            'toughnessBonus', t.toughness_bonus,
            'moraleBonus', t.morale_bonus,
            'costModifier', t.cost_modifier
        ) AS type,
        json_build_object(
            'sizeLevel', s.level_name,
            'unitSize', s.unit_size,
            'costModifier', s.cost_modifier
        ) AS size,
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
        FROM units u
        LEFT JOIN unit_ancestries a
            ON a.id = u.ancestry_id
        LEFT JOIN unit_experience_levels x
            ON x.id = u.experience_id
        LEFT JOIN unit_equipment_levels e
            ON e.id = u.equipment_id
        LEFT JOIN unit_types t 
            ON t.id = u.type_id
        LEFT JOIN unit_size_levels s
            ON s.id = u.size_id
        LEFT JOIN ancestry_trait_relations r
            ON r.ancestry_id = u.ancestry_id
        LEFT JOIN unit_traits tr
            ON tr.id = r.trait_id
        WHERE u.user_id = %s
        GROUP BY 
            u.id,
            u.unit_name,
            u.stronghold_id,
            u.user_id,
            u.casualties,
            u.mercenary,
            u.created_at,
            a.ancestry_name,   
            a.attack_bonus,
            a.power_bonus,
            a.defense_bonus,
            a.toughness_bonus,
            x.level_name,
            x.attack_bonus,
            x.toughness_bonus,
            x.morale_bonus,
            e.level_name,
            e.power_bonus,
            e.defense_bonus,
            t.type_name,
            t.attack_bonus,
            t.power_bonus,
            t.defense_bonus,
            t.toughness_bonus,
            t.morale_bonus,
            t.cost_modifier,
            s.level_name,
            s.unit_size,
            s.cost_modifier;
    """
)

GET_UNITS_BY_USER_AND_STRONGHOLD_ID = (
    """SELECT
        u.id AS "unit_id",
        u.unit_name AS "name",
        u.stronghold_id,
        u.user_id,
        u.casualties,
        u.mercenary AS "isMercenary",
        u.created_at AS "creationDate",
        json_build_object(
            'name', a.ancestry_name,
            'attackBonus', a.attack_bonus,
            'powerBonus', a.power_bonus,
            'defenseBonus', a.defense_bonus,
            'toughnessBonus', a.toughness_bonus,
            'moraleBonus', a.morale_bonus
        ) AS ancestry,
        json_build_object(
            'name', x.level_name,
            'attackBonus', x.attack_bonus,
            'toughnessBonus', x.toughness_bonus,
            'moraleBonus', x.morale_bonus
        ) AS experience,
        json_build_object(
            'name', e.level_name,
            'powerBonus', e.power_bonus,
            'defenseBonus', e.defense_bonus
        ) AS equipment,
        json_build_object(
            'name', t.type_name,
            'attackBonus', t.attack_bonus,
            'powerBonus', t.power_bonus,
            'defenseBonus', t.defense_bonus,
            'toughnessBonus', t.toughness_bonus,
            'moraleBonus', t.morale_bonus,
            'costModifier', t.cost_modifier
        ) AS type,
        json_build_object(
            'sizeLevel', s.level_name,
            'unitSize', s.unit_size,
            'costModifier', s.cost_modifier
        ) AS size,
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
        FROM units u
        LEFT JOIN unit_ancestries a
            ON a.id = u.ancestry_id
        LEFT JOIN unit_experience_levels x
            ON x.id = u.experience_id
        LEFT JOIN unit_equipment_levels e
            ON e.id = u.equipment_id
        LEFT JOIN unit_types t 
            ON t.id = u.type_id
        LEFT JOIN unit_size_levels s
            ON s.id = u.size_id
        LEFT JOIN ancestry_trait_relations r
            ON r.ancestry_id = u.ancestry_id
        LEFT JOIN unit_traits tr
            ON tr.id = r.trait_id
        WHERE u.user_id = %s 
        AND u.stronghold_id = %s
        GROUP BY 
            u.id,
            u.unit_name,
            u.stronghold_id,
            u.user_id,
            u.casualties,
            u.mercenary,
            u.created_at,
            a.ancestry_name,   
            a.attack_bonus,
            a.power_bonus,
            a.defense_bonus,
            a.toughness_bonus,
            x.level_name,
            x.attack_bonus,
            x.toughness_bonus,
            x.morale_bonus,
            e.level_name,
            e.power_bonus,
            e.defense_bonus,
            t.type_name,
            t.attack_bonus,
            t.power_bonus,
            t.defense_bonus,
            t.toughness_bonus,
            t.morale_bonus,
            t.cost_modifier,
            s.level_name,
            s.unit_size,
            s.cost_modifier;
    """
)
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
        u.id,
        u.unit_name AS "name",
        u.stronghold_id,
        u.user_id,
        a.ancestry_name AS "ancestry",
        x.level_name AS "experience",
        e.level_name AS "equipment",
        t.type_name AS "type",
        s.unit_size AS "size",
        u.casualties,
        u.mercenary,
        u.created_at
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
        WHERE u.user_id = %s;
    """
)
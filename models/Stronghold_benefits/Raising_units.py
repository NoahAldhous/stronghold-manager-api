CREATE_RAISING_UNITS_TABLE = (
    """CREATE TABLE IF NOT EXISTS raising_units (
        id SERIAL PRIMARY KEY,
        low_number INT NOT NULL,
        high_number INT NOT NULL,
        experience_id INT NOT NULL REFERENCES unit_experience_levels(id),
        equipment_id INT NOT NULL REFERENCES unit_equipment_levels(id),
        type_id INT NOT NULL REFERENCES unit_types(id),
        keep_type TEXT  
    );"""
)

CREATE_UNITS_RAISED_TABLE = (
    """CREATE TABLE IF NOT EXISTS units_raised (
        id SERIAL PRIMARY KEY,
        stronghold_id INT NOT NULL REFERENCES strongholds(id) ON DELETE CASCADE,
        unit_id INT NOT NULL REFERENCES units(id) ON DELETE CASCADE,
        raising_unit_id INT NOT NULL REFERENCES raising_units(id)
    );"""
)

CREATE_STRONGHOLD_RAISING_UNITS_STATUS_TABLE = (
    """CREATE TABLE IF NOT EXISTS stronghold_raising_units_status (
        id SERIAL PRIMARY KEY,
        stronghold_id INT UNIQUE NOT NULL REFERENCES strongholds(id) ON DELETE CASCADE,
        current_units INT NOT NULL,
        max_units INT NOT NULL,
        has_raised_all_units BOOLEAN    
    );"""
)

INSERT_STRONGHOLD_RAISING_UNITS_STATUS = (
    """INSERT INTO stronghold_raising_units_status (
        stronghold_id,
        current_units,
        max_units,
        has_raised_all_units    
        ) VALUES (
            %s,
            %s,
            %s,
            %s
        );
    """
)

GET_STRONGHOLD_RAISING_UNITS_STATUS_BY_STRONGHOLD_ID = (
    """SELECT * FROM stronghold_raising_units_status WHERE stronghold_id = %s;"""
)

POPULATE_RAISING_UNITS_TABLE = (
    """INSERT INTO raising_units (
        low_number,
        high_number,
        experience_id,
        equipment_id,
        type_id,
        keep_type 
    ) SELECT
        r.low_number,
        r.high_number,
        x.id,
        e.id,
        t.id,
        r.keep_type
    FROM (
        VALUES 
            (
                1,
                12,
                'green',
                'light',
                'infantry', 
                'keep'
            ),
            (
                13,
                24,
                'green',
                'medium',
                'infantry', 
                'keep'
            ),
            (
                25,
                34,
                'regular',
                'light',
                'infantry', 
                'keep'
            ),
            (
                35,
                44,
                'regular',
                'medium',
                'infantry', 
                'keep'
            ),
            (
                45,
                46,
                'seasoned',
                'medium',
                'infantry', 
                'keep'
            ),
            (
                47,
                48,
                'seasoned',
                'heavy',
                'infantry', 
                'keep'
            ),
            (
                49,
                57,
                'green',
                'light',
                'archers', 
                'keep'
            ),
            (
                58,
                66,
                'green',
                'medium',
                'archers', 
                'keep'
            ),
            (
                67,
                72,
                'regular',
                'light',
                'archers', 
                'keep'
            ),
            (
                73,
                78,
                'regular',
                'medium',
                'archers', 
                'keep'
            ),
            (
                79,
                86,
                'regular',
                'light',
                'cavalry', 
                'keep'
            ),
            (
                87,
                95,
                'regular',
                'medium',
                'cavalry', 
                'keep'
            ),
            (
                96,
                100,
                'regular',
                'medium',
                'cavalry', 
                'keep'
            ),
            (
                1,
                3,
                'green',
                'light',
                'infantry', 
                'camp'
            ),
            (
                4,
                6,
                'regular',
                'light',
                'infantry', 
                'camp'
            ),
            (
                7,
                8,
                'green',
                'light',
                'archers', 
                'camp'
            ),
            (
                9,
                10,
                'regular',
                'light',
                'archers', 
                'camp'
            ),
            (
                11,
                11,
                'regular',
                'light',
                'cavalry', 
                'camp'
            ),
            (
                12,
                12,
                'seasoned',
                'light',
                'cavalry', 
                'camp'
            )
    ) AS r (low_number, high_number, experience, equipment, unit_type, keep_type)
        JOIN unit_experience_levels x
            ON r.experience = x.level_name
        JOIN unit_equipment_levels e
            ON r.equipment = e.level_name
        JOIN unit_types t
            ON r.unit_type = t.type_name
    ;"""
)

GET_UNITS_RAISED_BY_KEEP_TYPE = (
    """SELECT
        r.id,
        r.low_number AS "lowNumber",
        r.high_number AS "highNumber",
        r.keep_type AS "keepType",
        json_build_object(
            'experience', x.level_name,
            'equipment', e.level_name,
            'type', t.type_name
        ) AS unit
        FROM raising_units r
        LEFT JOIN unit_experience_levels x
            ON r.experience_id = x.id
        LEFT JOIN unit_equipment_levels e
            ON r.equipment_id = e.id
        LEFT JOIN unit_types t
            ON r.type_id = t.id
        WHERE keep_type = %s
    ;"""
)
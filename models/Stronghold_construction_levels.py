CREATE_STRONGHOLD_CONSTRUCTION_LEVELS_TABLE = (
    "CREATE TABLE IF NOT EXISTS stronghold_construction_levels (id SERIAL PRIMARY KEY, stronghold_level INT, stronghold_type_id INT, cost_to_build INTEGER, time_to_build INTEGER, fortification_morale_bonus INTEGER, FOREIGN KEY(stronghold_type_id) REFERENCES stronghold_types(id));"
)

POPULATE_STRONGHOLD_CONSTRUCTION_LEVELS_TABLE = (
    """INSERT INTO stronghold_construction_levels (
        stronghold_level,
        stronghold_type_id,
        cost_to_build,
        time_to_build,
        fortification_morale_bonus    
    ) VALUES
        (
            1, (SELECT id FROM stronghold_types WHERE type_name = keep), 10000, 150, 2
        ),
        (
            2, (SELECT id FROM stronghold_types WHERE type_name = keep), 5000, 50, 4
        ),
        (
            3, (SELECT id FROM stronghold_types WHERE type_name = keep), 10000, 100, 6
        ),
        (
            4, (SELECT id FROM stronghold_types WHERE type_name = keep), 15000, 150, 8
        ),
        (
            5, (SELECT id FROM stronghold_types WHERE type_name = keep), 20000, 200, 10
        ),
        (
            1, (SELECT id FROM stronghold_types WHERE type_name = tower), 8000, 120, 1
        ),
        (
            2, (SELECT id FROM stronghold_types WHERE type_name = tower), 3000, 40, 2
        ),
        (
            3, (SELECT id FROM stronghold_types WHERE type_name = tower), 6000, 80, 3
        ),
        (
            4, (SELECT id FROM stronghold_types WHERE type_name = tower), 12000, 120, 4
        ),
        (
            5, (SELECT id FROM stronghold_types WHERE type_name = tower), 18000, 160, 5
        ),
        (
            1, (SELECT id FROM stronghold_types WHERE type_name = temple), 8000, 120, 1
        ),
        (
            2, (SELECT id FROM stronghold_types WHERE type_name = temple), 3000, 40, 2
        ),
        (
            3, (SELECT id FROM stronghold_types WHERE type_name = temple), 6000, 80, 3
        ),
        (
            4, (SELECT id FROM stronghold_types WHERE type_name = temple), 12000, 120, 4
        ),
        (
            5, (SELECT id FROM stronghold_types WHERE type_name = temple), 18000, 160, 5
        ),
        (
            1, (SELECT id FROM stronghold_types WHERE type_name = establishment), 6000, 90, 0
        ),
        (
            2, (SELECT id FROM stronghold_types WHERE type_name = establishment), 2000, 30, 0
        ),
        (
            3, (SELECT id FROM stronghold_types WHERE type_name = establishment), 4000, 60, 0
        ),
        (
            4, (SELECT id FROM stronghold_types WHERE type_name = establishment), 6000, 90, 0
        ),
        (
            5, (SELECT id FROM stronghold_types WHERE type_name = establishment), 8000, 120, 0
        );
    """
)

INSERT_STRONGHOLD_CONSTRUCTION_LEVEL = (
    "INSERT INTO stronghold_construction_levels (stronghold_level, stronghold_type_id, cost_to_build, time_to_build, fortification_morale_bonus) VALUES (%s, (SELECT id FROM stronghold_types WHERE type_name = %s), %s, %s, %s);"
)

GET_ALL_STRONGHOLD_CONSTRUCTION_LEVELS = (
    "SELECT * FROM stronghold_construction_levels;"
)

GET_STRONGHOLD_CONSTRUCTION_LEVELS_BY_TYPE_ID = (
    "SELECT * FROM stronghold_construction_levels WHERE stronghold_type_id = %s;"
)

GET_STRONGHOLD_CONSTRUCTION_BY_LEVEL = (
    "SELECT * FROM stronghold_construction_levels WHERE stronghold_level = %s;"
)

UPDATE_STRONGHOLD_CONSTRUCTION_LEVEL_BY_ID = (
    "UPDATE stronghold_construction_levels SET cost_to_build = %s, time_to_build = %s, fortification_morale_bonus = %s WHERE id = %s;"
)

DELETE_STRONGHOLD_CONSTRUCTION_LEVEL_BY_ID = (
    "DELETE FROM stronghold_construction_levels WHERE id = %s;"
)

CLEAR_STRONGHOLD_CONSTRUCTION_LEVELS_TABLE = (
    "DELETE FROM stronghold_construction_levels;"
)
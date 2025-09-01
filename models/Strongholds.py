CREATE_STRONGHOLDS_TABLE = (
    "CREATE TABLE IF NOT EXISTS strongholds (id SERIAL PRIMARY KEY, user_id INT, FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE, stronghold_name TEXT, owner_name TEXT, stronghold_level INTEGER, stronghold_type_id INT, FOREIGN KEY(stronghold_type_id) REFERENCES stronghold_types(id), created_at TIMESTAMP);"
)

INSERT_STRONGHOLD_RETURN_ID = (    
    "INSERT INTO strongholds (user_id, stronghold_name, owner_name, stronghold_level, stronghold_type_id, created_at) VALUES (%s, %s, %s, %s, (SELECT id FROM stronghold_types WHERE type_name = %s), %s) RETURNING id;"
)

GET_STRONGHOLDS_BY_USER_ID = (
    "SELECT id, stronghold_name, owner_name, stronghold_level, (SELECT type_name AS stronghold_type FROM stronghold_types WHERE id = stronghold_type_id) FROM strongholds WHERE user_id = %s;"
)

GET_STRONGHOLD_BY_ID = (
    "SELECT * FROM strongholds WHERE id = %s;"
)

GET_STRONGHOLD_BY_ID_RETURN_ALL_STRONGHOLD_DATA = (
    """SELECT
        s.id,
        s.stronghold_name,
        s.owner_name,
        s.stronghold_level,
        c.cost_to_build as upgrade_cost,
        (
            SELECT type_name AS stronghold_type 
            FROM stronghold_types 
            WHERE id = s.stronghold_type_id
        ),
        (
            SELECT stronghold_size
            FROM stronghold_size_levels
            WHERE stronghold_type_id = s.stronghold_type_id
            AND stronghold_level = s.stronghold_level
        ),
        json_build_object(
            'toughness', (
                SELECT toughness FROM stronghold_toughness_levels 
                WHERE stronghold_level = s.stronghold_level 
                AND stronghold_type_id = s.stronghold_type_id
            ),
            'morale_bonus', (
                SELECT fortification_morale_bonus FROM stronghold_construction_levels
                WHERE stronghold_level = s.stronghold_level
                AND stronghold_type_id = s.stronghold_type_id
            )
        ) AS stats,
        json_agg(
            json_build_object(
                'title', f.feature_name,
                'description', f.feature_description
            )
        ) AS features 
        FROM strongholds s
        LEFT JOIN stronghold_type_features f
            ON s.stronghold_type_id = f.stronghold_type_id
        LEFT JOIN stronghold_construction_levels c
            ON s.stronghold_type_id = c.stronghold_type_id
            AND s.stronghold_level + 1 = c.stronghold_level 
        WHERE s.id = %s
        GROUP BY s.id, c.cost_to_build;
    """
)

DELETE_STRONGHOLD_BY_ID = (
    "DELETE FROM strongholds WHERE id = %s;"
)

DELETE_STRONGHOLDS_TABLE = (
    "DROP TABLE strongholds;"
)
CREATE_STRONGHOLDS_TABLE = (
    "CREATE TABLE IF NOT EXISTS strongholds (id SERIAL PRIMARY KEY, user_id INT, FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE, stronghold_name TEXT, owner_name TEXT, stronghold_level INTEGER, stronghold_type_id INT, FOREIGN KEY(stronghold_type_id) REFERENCES stronghold_types(id), created_at TIMESTAMP);"
)

INSERT_STRONGHOLD_RETURN_ID = (    
    """INSERT INTO strongholds (
        user_id, 
        stronghold_name, 
        owner_name, 
        stronghold_level, 
        stronghold_type_id,
        stronghold_class_id, 
        created_at
    ) VALUES (
        %s, 
        %s, 
        %s, 
        %s, 
        (SELECT id 
            FROM stronghold_types 
            WHERE type_name = %s),
        (SELECT id
            FROM stronghold_classes
            WHERE class_name = %s),
        %s
    ) 
    RETURNING id;"""
)

GET_STRONGHOLDS_BY_USER_ID = (
    """SELECT 
        id, 
        stronghold_name AS "name", 
        owner_name AS "ownerName", 
        stronghold_level AS "level", 
        (SELECT type_name AS "type" 
            FROM stronghold_types 
            WHERE id = stronghold_type_id
        )
        (SELECT 
            class_name AS "ownerClass",
            class_stronghold_name AS "classStrongholdName"
            FROM stronghold_classes
            WHERE id = stronghold_class_id
        )
        FROM strongholds WHERE user_id = %s;"""
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
        (
            SELECT json_agg(json_build_object(
                'title', features.feature_name,
                'description', features.feature_description
            ))
            FROM stronghold_type_features AS features
            WHERE features.stronghold_type_id = s.stronghold_type_id
        ) AS features,
        json_build_object(
            'name', classes.class_name,
            'stronghold_name', classes.class_stronghold_name,
            'description', classes.class_stronghold_description,
            'stronghold_actions', (
                SELECT json_agg(
                    json_build_object(
                        'name', actions.action_name,
                        'description', actions.action_description
                    )
                ) FROM class_stronghold_actions AS actions
                WHERE actions.stronghold_class_id = s.stronghold_class_id
            ),
            'demesne_effects', (
                SELECT json_agg(
                    json_build_object(
                        'description', effects.effect_description
                    )
                ) FROM class_demesne_effects AS effects
                WHERE effects.stronghold_class_id = s.stronghold_class_id
            ),
            'class_feature_improvement', (
                json_build_object(
                    'name', improvements.improvement_name,
                    'description', improvements.improvement_description,
                    'restriction', restrictions.restriction_description
                )
            )
        ) AS class
        FROM strongholds s
        LEFT JOIN stronghold_construction_levels c
            ON s.stronghold_type_id = c.stronghold_type_id
            AND s.stronghold_level + 1 = c.stronghold_level 
        LEFT JOIN stronghold_classes AS classes
            ON s.stronghold_class_id = classes.id
        LEFT JOIN class_feature_improvements AS improvements
            ON  s.stronghold_class_id = improvements.stronghold_class_id
        LEFT JOIN class_feature_restrictions AS restrictions
            ON improvements.improvement_restriction_id = restrictions.id
        WHERE s.id = %s
        GROUP BY 
            s.id, 
            c.cost_to_build, 
            classes.class_name, 
            classes.class_stronghold_name, 
            classes.class_stronghold_description,
            improvements.improvement_name,
            improvements.improvement_description,
            restrictions.restriction_description;
    """
)

DELETE_STRONGHOLD_BY_ID = (
    "DELETE FROM strongholds WHERE id = %s;"
)

DELETE_STRONGHOLDS_TABLE = (
    "DROP TABLE strongholds;"
)
CREATE_STRONGHOLD_TYPES_TABLE = (
    "CREATE TABLE IF NOT EXISTS stronghold_types (id SERIAL PRIMARY KEY, type_name TEXT UNIQUE);"
)

INSERT_STRONGHOLD_TYPES = (
    "INSERT INTO stronghold_types (type_name) VALUES ('keep'),('tower'),('temple'),('establishment'),('castle') RETURNING *;"
)

ADD_NEW_STRONGHOLD_TYPE = (
    "INSERT INTO stronghold_types (type_name) VALUES (%s) RETURNING *"
)

GET_ALL_STRONGHOLD_TYPES = (
    "SELECT * FROM stronghold_types;"
)

GET_STRONGHOLD_TYPE_AND_FEATURES = (
    """SELECT 
        st.id,
        st.type_name,
        COALESCE(
            json_agg(
                json_build_object(
                    'feature_name', f.feature_name,
                    'feature_description', f.feature_description
                )
            ) FILTER (WHERE f.feature_name IS NOT NULL),
            '[]'
        ) AS features
        FROM stronghold_types st
        LEFT JOIN stronghold_type_features f
            ON st.id = f.type_id
        WHERE st.id = %s 
        GROUP BY st.id, st.type_name;
    """
)

UPDATE_STRONGHOLD_TYPE_BY_ID = (
    "UPDATE stronghold_types SET type_name = %s WHERE id = %s;"
)

DELETE_STRONGHOLD_TYPE_BY_ID = (
    "DELETE FROM stronghold_types WHERE ID = %s;"
)

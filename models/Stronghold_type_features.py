CREATE_STRONGHOLD_TYPE_FEATURES_TABLE = (
    "CREATE TABLE IF NOT EXISTS stronghold_type_features (id SERIAL PRIMARY KEY, FOREIGN KEY(stronghold_type_id) REFERENCES stronghold_types(id), feature_name TEXT, feature_description TEXT);"
)

GET_STRONGHOLD_TYPE_FEATURE_BY_ID = (
    "SELECT DISTINCT FROM stronghold_type_features WHERE id = %s;"
)

GET_STRONGHOLD_TYPE_FEATURE_BY_TYPE_ID = (
    "SELECT * FROM stronghold_type_features WHERE stronghold_type_id = %s;"
)

GET_ALL_STRONGHOLD_TYPE_FEATURES = (
    "SELECT * FROM stronghold_type_features;"
)

UPDATE_STRONGHOLD_TYPE_FEATURE_BY_ID = (
    "UPDATE stronghold_type_features SET feature_name = %s, feature_description = %s WHERE id = %s;"
)

DELETE_STRONGHOLD_TYPE_FEATURE_BY_ID = (
    "DELETE FROM stronghold_type_features WHERE ID = %s;"
)

INSERT_STRONGHOLD_TYPE_FEATURES = (
    "INSERT INTO stronghold_type_features (stronghold_type_id, feature_name, feature_description) VALUES (1, 'Raising Units', 'raising units decription'), (1, 'Training', 'training description'), (2, 'Spell Crafting')  RETURNING id"
)


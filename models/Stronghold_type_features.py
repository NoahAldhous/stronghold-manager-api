CREATE_STRONGHOLD_TYPE_FEATURES_TABLE = (
    "CREATE TABLE IF NOT EXISTS stronghold_type_features (id SERIAL PRIMARY KEY, FOREIGN KEY(stronghold_type_id) REFERENCES stronghold_types(id), feature_name TEXT, feature_description TEXT);"
)

INSERT_STRONGHOLD_TYPE_FEATURES = (
    "INSERT INTO stronghold_type_features (stronghold_type_id, feature_name, feature_description) VALUES (1, 'Raising Units', 'raising units decription'), (1, 'Training', 'training description'), (2, 'Spell Crafting')  RETURNING id"
)
CREATE_STRONGHOLDS_TABLE = (
    "CREATE TABLE IF NOT EXISTS strongholds (id SERIAL PRIMARY KEY, FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE, stronghold_name TEXT, stronghold_level INTEGER, FOREIGN KEY(stronghold_type_id) REFERENCES stronghold_types(id), FOREIGN KEY(stronghold_subtype_id) REFERENCES stronghold_subtypes(id), FOREIGN KEY(stronghold_class_id) REFERENCES stronghold_classes(id), class_feature_uses INTEGER, created_at TIMESTAMP);"
)

INSERT_STRONGHOLD = (    
    "INSERT INTO strongholds (stronghold_name, created_at) VALUES (%s, %s);"
)
from flask import Flask
from routes.users_bp import users_bp
from routes.strongholds_bp import strongholds_bp
from routes.stronghold_types_bp import stronghold_types_bp
from routes.stronghold_type_features_bp import stronghold_type_features_bp
from routes.stronghold_toughness_levels_bp import stronghold_toughness_levels_bp
from routes.stronghold_construction_levels_bp import stronghold_construction_levels_bp

# CREATE_CLASS_STRONGHOLD_ACTIONS_TABLE = (
#     "CREATE TABLE IF NOT EXISTS class_stronghold_actions (id SERIAL PRIMARY KEY, FOREIGN KEY(stronghold_class_id) REFERENCES stronghold_classes(id), action_description TEXT);"
# )

# CREATE_CLASS_DEMESNE_EFFECTS_TABLE = (
#     "CREATE TABLE IF NOT EXISTS class_demesne_effects (id SERIAL PRIMARY KEY, FOREIGN KEY(stronghold_class_id) REFERENCES stronghold_classes(id), effect_description TEXT);"
# )

# CREATE_CLASS_FEATURE_IMPROVEMENTS_TABLE = (
#     "CREATE TABLE IF NOT EXISTS class_feature_improvements (id SERIAL PRIMARY KEY, FOREIGN KEY(stronghold_class_id) REFERENCES stronghold_classes(id), improvement_name TEXT, improvement_description TEXT);"
# )

# CREATE_STRONGHOLD_CLASSES_TABLE = (
#     "CREATE TABLE IF NOT EXISTS stronghold_classes (id SERIAL PRIMARY KEY, class_name TEXT, class_stronghold_name TEXT);"
# )

# CREATE_STRONGHOLD_SUBTYPES_TABLE = (
#     "CREATE TABLE IF NOT EXISTS stronghold_subtypes (id SERIAL PRIMARY KEY, subtype_name TEXT);"
# )

app = Flask(__name__)

# Root route
@app.get("/")
def default_route():
    return "hello world!"

# Blueprint routes
app.register_blueprint(users_bp, url_prefix="/users")
app.register_blueprint(strongholds_bp, url_prefix="/strongholds")
app.register_blueprint(stronghold_types_bp, url_prefix="/stronghold_types")
app.register_blueprint(stronghold_type_features_bp, url_prefix="/stronghold_type_features")
app.register_blueprint(stronghold_toughness_levels_bp, url_prefix="/stronghold_toughness_levels")
app.register_blueprint(stronghold_construction_levels_bp, url_prefix="/stronghold_construction_levels")

if __name__ == "__main__":
    app.run()
from flask import Flask
from routes.users_bp import users_bp
from routes.strongholds_bp import strongholds_bp
from routes.stronghold_types_bp import stronghold_types_bp

# CREATE_STRONGHOLD_CONSTRUCTION_LEVELS_TABLE = (
#     "CREATE TABLE IF NOT EXISTS stronghold_construction_levels (id SERIAL PRIMARY KEY, stronghold_level INTEGER, FOREIGN KEY(stronghold_type_id) REFERENCES stronghold_types(id), cost_to_build INTEGER, time_to_build INTEGER, fortification_morale_bonus INTEGER);"
# )

# CREATE_STRONGHOLD_SIZE_LEVELS_TABLE = (
#     "CREATE TABLE IF NOT EXISTS stronghold_size_levels (id SERIAL PRIMARY KEY, stronghold_level INTEGER, FOREIGN KEY(stronghold_type_id) REFERENCES stronghold_types(id), stronghold_size INTEGER);"
# )

# CREATE_CLASS_STRONGHOLD_ACTIONS_TABLE = (
#     "CREATE TABLE IF NOT EXISTS class_stronghold_actions (id SERIAL PRIMARY KEY, FOREIGN KEY(stronghold_class_id) REFERENCES stronghold_classes(id), action_description TEXT);"
# )

# CREATE_CLASS_DEMESNE_EFFECTS_TABLE = (
#     "CREATE TABLE IF NOT EXISTS class_demesne_effects (id SERIAL PRIMARY KEY, FOREIGN KEY(stronghold_class_id) REFERENCES stronghold_classes(id), effect_description TEXT);"
# )

# CREATE_CLASS_FEATURE_IMPROVEMENTS_TABLE = (
#     "CREATE TABLE IF NOT EXISTS class_feature_improvements (id SERIAL PRIMARY KEY, FOREIGN KEY(stronghold_class_id) REFERENCES stronghold_classes(id), improvement_name TEXT, improvement_description TEXT);"
# )

# CREATE_STRONGHOLD_TOUGHNESS_LEVELS_TABLE = (
#     "CREATE TABLE IF NOT EXISTS stronghold_toughness_levels (id SERIAL PRIMARY KEY, level INTEGER, FOREIGN KEY(stronghold_class_id) REFERENCES stronghold_classes(id), stronghold_toughness INTEGER);"
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

if __name__ == "__main__":
    app.run()
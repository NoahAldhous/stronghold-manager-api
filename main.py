from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from utils import config
from utils.db import connection_pool
from routes.users_bp import users_bp
from routes.strongholds_bp import strongholds_bp
from routes.stronghold_types_bp import stronghold_types_bp
from routes.stronghold_type_features_bp import stronghold_type_features_bp
from routes.stronghold_toughness_levels_bp import stronghold_toughness_levels_bp
from routes.stronghold_construction_levels_bp import stronghold_construction_levels_bp
from routes.stronghold_size_levels_bp import stronghold_size_levels_bp
from routes.stronghold_classes_bp import stronghold_classes_bp
from routes.class_stronghold_actions_bp import class_stronghold_actions_bp
from routes.class_demesne_effects_bp import class_demesne_effects_bp
from routes.class_feature_improvements_bp import class_feature_improvements_bp
from routes.stronghold_type_stats_bp import stronghold_type_stats_bp
from routes.stronghold_treasury_bp import stronghold_treasury_bp
from routes.units.units_bp import units_bp

app = Flask(__name__)
#set up JWT for auth
app.config["JWT_SECRET_KEY"] = config.JWT_SECRET_KEY
jwt = JWTManager(app)
#Allow cross-origin requests
CORS(app, origins=[
    "http://localhost:3000",
    config.CLIENT_URL 
])

# Root route
@app.get("/")
def default_route():
    return "hello world!"

@app.teardown_appcontext
def close_connection_pool(exception):
    if connection_pool:
        connection_pool.closeall()

# BLUEPRINT ROUTES
# /strongholds
stronghold_types_bp.register_blueprint(stronghold_type_stats_bp, url_prefix="/stats")
stronghold_types_bp.register_blueprint(stronghold_type_features_bp, url_prefix="/features")
stronghold_classes_bp.register_blueprint(class_feature_improvements_bp, url_prefix="/features")
stronghold_classes_bp.register_blueprint(class_stronghold_actions_bp, url_prefix="/actions")
stronghold_classes_bp.register_blueprint(class_demesne_effects_bp, url_prefix="/demesne_effects")

strongholds_bp.register_blueprint(stronghold_treasury_bp, url_prefix="/treasury")
strongholds_bp.register_blueprint(stronghold_types_bp, url_prefix="/types")
strongholds_bp.register_blueprint(stronghold_toughness_levels_bp, url_prefix="/toughness")
strongholds_bp.register_blueprint(stronghold_construction_levels_bp, url_prefix="/construction")
strongholds_bp.register_blueprint(stronghold_size_levels_bp, url_prefix="/size")
strongholds_bp.register_blueprint(stronghold_classes_bp, url_prefix="/classes")

app.register_blueprint(strongholds_bp, url_prefix="/strongholds")
app.register_blueprint(users_bp, url_prefix="/users")
app.register_blueprint(units_bp, url_prefix="/units")

if __name__ == "__main__":
    app.run()
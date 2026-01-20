from flask import Flask, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from utils import config
from utils.db import close_pool
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
from routes.stronghold_benefits.raising_units_bp import raising_units_bp
from routes.artisans import alchemy_tests_bp, artisan_bonuses_bp, artisan_shops_bp, artisan_upgrade_costs_bp, stronghold_artisans_bp
import atexit

app = Flask(__name__)

atexit.register(close_pool)
    
@app.teardown_appcontext
def on_teardown(exception):
    print("Teardown with exception", exception)
  
# Dev-only manual shutdown route- avoid in prod
@app.route("/shutdown")
def shutdown():
    try:   
        close_pool()
    except Exception as e:
        print(f"Error closing pool manually: {e}")
        
    func = request.environ.get("werkzeug.server.shutdown")
    if func:
        func()
    return "Server shutting down..."
      
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


# BLUEPRINT ROUTES
# /artisans
stronghold_artisans_bp.register_blueprint(alchemy_tests_bp, url_prefix="/alchemy_tests")
stronghold_artisans_bp.register_blueprint(artisan_bonuses_bp, url_prefix="/bonuses")
stronghold_artisans_bp.register_blueprint(artisan_shops_bp, url_prefix="/shops")
stronghold_artisans_bp.register_blueprint(artisan_upgrade_costs_bp, url_prefix="/upgade_costs")

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
strongholds_bp.register_blueprint(raising_units_bp, url_prefix="/raising_units")
strongholds_bp.register_blueprint(stronghold_artisans_bp, url_prefix="/artisans")

app.register_blueprint(strongholds_bp, url_prefix="/strongholds")
app.register_blueprint(users_bp, url_prefix="/users")
app.register_blueprint(units_bp, url_prefix="/units")

if __name__ == "__main__":
    app.run()
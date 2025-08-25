from flask import Flask
from routes.users_bp import users_bp
from routes.strongholds_bp import strongholds_bp
from routes.stronghold_types_bp import stronghold_types_bp
from routes.stronghold_type_features_bp import stronghold_type_features_bp
from routes.stronghold_toughness_levels_bp import stronghold_toughness_levels_bp
from routes.stronghold_construction_levels_bp import stronghold_construction_levels_bp
from routes.stronghold_size_levels_bp import stronghold_size_levels_bp

app = Flask(__name__)

# Root route
@app.get("/")
def default_route():
    return "hello world!"

# BLUEPRINT ROUTES
# /strongholds
stronghold_types_bp.register_blueprint(stronghold_type_features_bp, url_prefix="/features")
strongholds_bp.register_blueprint(stronghold_types_bp, url_prefix="/types")
strongholds_bp.register_blueprint(stronghold_toughness_levels_bp, url_prefix="/toughness")
strongholds_bp.register_blueprint(stronghold_construction_levels_bp, url_prefix="/construction")
strongholds_bp.register_blueprint(stronghold_size_levels_bp, url_prefix="/size")
app.register_blueprint(strongholds_bp, url_prefix="/strongholds")

# /users
app.register_blueprint(users_bp, url_prefix="/users")

if __name__ == "__main__":
    app.run()
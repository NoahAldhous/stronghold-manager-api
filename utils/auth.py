from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from flask import jsonify

# Converts password into randomised string/hash
def hash_password(plain):
    return generate_password_hash(plain, method="pbkdf2:sha256", salt_length=16)

# Compares password hash against login password and returns boolean
def verify_password(pw, pw_hash):
    return check_password_hash(pw_hash, pw)

# Decorator for endpoints that creates role-based restrictions
def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        # check there is a valid JWT
        verify_jwt_in_request()
        # pull decoded claims out of token
        claims = get_jwt()
        # get 'role' and check if equals 'admin' - if not, stop and return 403
        if claims.get("role") != "admin":
            return jsonify(msg="Permission not authorised, admins only"), 403
        # if all good (admin logged in) run endpoint code
        return fn(*args, **kwargs)
    return wrapper
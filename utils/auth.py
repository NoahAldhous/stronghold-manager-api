from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from flask_jwt_extended import (get_jwt, jwt_required)
from flask import jsonify

# Converts password into randomised string/hash for storing in db
def hash_password(plain):
    return generate_password_hash(plain, method="pbkdf2:sha256", salt_length=16)

# Compares password hash against login password and returns boolean
def verify_password(pw, pw_hash):
    return check_password_hash(pw_hash, pw)

# Decorator for endpoints that creates role-based restrictions
def roles_required(*roles):
    def decorator(fn):    
        @wraps(fn)
        @jwt_required()
        def wrapper(*args, **kwargs):
            # pull decoded role out of token
            role = get_jwt().get("role")
            # get 'role' and check if equal to at least one of the roles provided - if not, stop and return 403
            if role not in roles:
                return jsonify(msg="Permission not authorised, admins only"), 403
            # if all good (authenticated and authorised) run endpoint code
            return fn(*args, **kwargs)
        return wrapper
    return decorator
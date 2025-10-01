from dotenv import load_dotenv
import os
from datetime import timedelta

# parse .env file and load environment variables
load_dotenv()
#This CANNOT be called url, it takes the env from smartpantry for some reason.
DB_URL = os.getenv("STRONGHOLD_DATABASE_URL")
CLIENT_URL = os.getenv("CLIENT_URL")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "fallback-dev-only-changeme")

# Optional hard-gate for dangerous endpoints
ALLOW_DANGEROUS_ENDPOINTS = os.getenv("ALLOW_DANGEROUS_ENDPOINTS", "false").lower() == "true"
# Optional extra lock
ADMIN_API_KEY = os.getenv("ADMIN_API_KEY")

#jwt expiration config
JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=15)
JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=7)
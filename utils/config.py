from dotenv import load_dotenv
import os

# parse .env file and load environment variables
load_dotenv()
#This CANNOT be called url, it takes the env from smartpantry for some reason.
DB_URL = os.getenv("STRONGHOLD_DATABASE_URL")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "fallback-dev-only-changeme")

# Optional hard-gate for dangerous endpoints
ALLOW_DANGEROUS_ENDPOINTS = os.getenv("ALLOW_DANGEROUS_ENDPOINTS", "false").lower() == "true"
# Optional extra lock
ADMIN_API_KEY = os.getenv("ADMIN_API_KEY")

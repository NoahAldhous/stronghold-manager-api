from dotenv import load_dotenv
import os

# parse .env file and load environment variables
load_dotenv()
#This CANNOT be called url, it takes the env from smartpantry for some reason.
DB_URL = os.getenv("STRONGHOLD_DATABASE_URL")

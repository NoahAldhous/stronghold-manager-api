import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()
#This CANNOT be called url, it takes the env from smartpantry for some reason.
dburl = os.getenv("STRONGHOLD_DATABASE_URL")
connection = psycopg2.connect(dburl)
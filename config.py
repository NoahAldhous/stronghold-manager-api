import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()
dburl = os.getenv("STRONGHOLD_DATABASE_URL")
connection = psycopg2.connect(dburl)
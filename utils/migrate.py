import psycopg2
import os
from utils import config

connection = psycopg2.connect(config.DB_URL)
cursor = connection.cursor()

# Create a table to track migrations
cursor.execute("""
    CREATE TABLE IF NOT EXISTS schema_migrations (
        id SERIAL PRIMARY KEY,
        filename TEXT UNIQUE NOT NULL,
        applied_at TIMESTAMP DEFAULT NOW()
    );         
""")
connection.commit()

# Run all new migrations
migration_dir = "utils/db_migrations"
files = sorted(f for f in os.listdir(migration_dir) if f.endswith(".sql"))

for f in files:
    cursor.execute("SELECT 1 FROM schema_migrations WHERE filename = %s", (f,))
    if cursor.fetchone():
        print(f"Skipping {f}, already applied.")
        continue
    
    print(f"Applying {f}...")
    with open(os.path.join(migration_dir, f), "r") as sql_file:
        cursor.execute(sql_file.read())
    cursor.execute("INSERT INTO schema_migrations (filename) VALUES (%s)", (f,))
    connection.commit()
    
cursor.close()
connection.close()
print("All migrations applied")
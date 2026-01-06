import sqlite3
from pathlib import Path
import os

from users import generate_users
from teams import generate_teams_and_memberships
from projects import generate_projects
from sections import generate_sections
from tasks import generate_tasks
from tasks import generate_subtasks
from comments import generate_comments

# Paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = PROJECT_ROOT / "output" / "asana_simulation.sqlite"
SCHEMA_PATH = PROJECT_ROOT / "schema.sql"

def create_database():
    if DB_PATH.exists():
        os.remove(DB_PATH)

    DB_PATH.parent.mkdir(exist_ok=True)
    conn = sqlite3.connect(DB_PATH)

    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        schema_sql = f.read()

    conn.executescript(schema_sql)
    conn.close()
    print("Database schema created successfully.")

def main():
    create_database()
    generate_users(DB_PATH)
    generate_teams_and_memberships(DB_PATH)
    generate_projects(DB_PATH)
    generate_sections(DB_PATH)
    generate_tasks(DB_PATH)
    generate_subtasks(DB_PATH)
    generate_comments(DB_PATH)

if __name__ == "__main__":
    main()

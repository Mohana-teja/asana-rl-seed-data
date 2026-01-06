import sqlite3
import random
from datetime import datetime, timedelta

PROJECT_TYPES = ["Product", "Marketing", "Operations", "Growth", "Infrastructure"]
PROJECT_STATUSES = ["active", "completed", "archived"]

def generate_projects(db_path, num_projects=120):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # fetch teams
    cursor.execute("SELECT team_id, organization_id FROM teams")
    teams = cursor.fetchall()

    projects = []

    for project_id in range(1, num_projects + 1):
        team_id, org_id = random.choice(teams)
        start_date = datetime.now() - timedelta(days=random.randint(30, 180))
        end_date = start_date + timedelta(days=random.randint(15, 120))

        status = random.choices(
            PROJECT_STATUSES,
            weights=[0.6, 0.3, 0.1],
            k=1
        )[0]

        projects.append((
            project_id,
            f"{random.choice(PROJECT_TYPES)} Project {project_id}",
            random.choice(PROJECT_TYPES),
            team_id,
            org_id,
            status,
            start_date,
            start_date.date(),
            end_date.date(),
            status == "active"
        ))

    cursor.executemany("""
        INSERT INTO projects (
            project_id, project_name, project_type,
            team_id, organization_id, status,
            created_at, start_date, end_date, is_active
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, projects)

    conn.commit()
    conn.close()

    print(f"{num_projects} projects generated.")

import sqlite3
import random
from datetime import datetime

TEAM_NAMES = [
    "Backend Engineering",
    "Frontend Engineering",
    "Mobile Engineering",
    "Product Management",
    "Design",
    "Marketing",
    "Growth",
    "Sales",
    "Customer Success",
    "Operations",
    "Data Science",
    "DevOps"
]

def generate_teams_and_memberships(db_path, num_teams=30):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # fetch users
    cursor.execute("SELECT user_id FROM users")
    user_ids = [row[0] for row in cursor.fetchall()]

    teams = []
    memberships = []

    for team_id in range(1, num_teams + 1):
        team_name = random.choice(TEAM_NAMES)
        teams.append((
            team_id,
            team_name,
            1,                  # organization_id
            datetime.now(),
            True
        ))

        # assign 5–20 users per team
        members = random.sample(user_ids, random.randint(5, 20))
        for user_id in members:
            memberships.append((
                team_id,
                user_id,
                datetime.now()
            ))

    cursor.executemany("""
        INSERT INTO teams (
            team_id, team_name, organization_id, created_at, is_active
        ) VALUES (?, ?, ?, ?, ?)
    """, teams)

    cursor.executemany("""
        INSERT INTO team_memberships (
            team_id, user_id, joined_at
        ) VALUES (?, ?, ?)
    """, memberships)

    conn.commit()
    conn.close()

    print(f"{num_teams} teams and memberships generated.")

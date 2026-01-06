import sqlite3
import random
from faker import Faker
from date_utils import random_past_date

fake = Faker()

ROLES = ["admin", "manager", "member"]
LOCATIONS = ["US", "India", "EU"]

def generate_users(db_path, num_users=7000):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    users = []

    for user_id in range(1, num_users + 1):
        role = random.choices(
            ROLES,
            weights=[0.05, 0.10, 0.85],
            k=1
        )[0]

        user = (
            user_id,
            fake.name(),
            f"user{user_id}@company.com",
            role,
            fake.job(),
            random.choice(LOCATIONS),
            random.choice([True, True, True, False]),
            random_past_date()
        )

        users.append(user)

    cursor.executemany("""
        INSERT INTO users (
            user_id, full_name, email, role,
            title, location, is_active, created_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, users)

    conn.commit()
    conn.close()

    print(f"{num_users} users generated.")

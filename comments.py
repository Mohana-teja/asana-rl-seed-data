import sqlite3
import random
from datetime import datetime, timedelta

COMMENT_TEMPLATES = [
    "Please review this.",
    "This is blocked, need input.",
    "Completed as discussed.",
    "Working on this now.",
    "Can we prioritize this?",
    "Looks good to me."
]

def generate_comments(db_path, max_comments_per_task=3):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT task_id, created_at FROM tasks")
    tasks = cursor.fetchall()

    cursor.execute("SELECT user_id FROM users")
    users = [row[0] for row in cursor.fetchall()]

    comments = []
    comment_id = 1

    for task_id, created_at in tasks:
        if random.random() < 0.4:  # not all tasks have comments
            for _ in range(random.randint(1, max_comments_per_task)):
                comments.append((
                    comment_id,
                    task_id,
                    random.choice(users),
                    random.choice(COMMENT_TEMPLATES),
                    datetime.fromisoformat(created_at) + timedelta(days=random.randint(0, 5))
                ))
                comment_id += 1

    cursor.executemany("""
        INSERT INTO comments (
            comment_id, task_id, author_id, content, created_at
        ) VALUES (?, ?, ?, ?, ?)
    """, comments)

    conn.commit()
    conn.close()

    print(f"{len(comments)} comments generated.")

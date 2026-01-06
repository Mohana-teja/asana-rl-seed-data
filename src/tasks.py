import sqlite3
import random
from datetime import datetime, timedelta

TASK_STATUSES = ["open", "in_progress", "completed"]
PRIORITIES = ["low", "medium", "high"]

def generate_tasks(db_path, num_tasks=5000):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT project_id FROM projects")
    project_ids = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT section_id FROM sections")
    section_ids = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT user_id FROM users WHERE is_active = 1")
    user_ids = [row[0] for row in cursor.fetchall()]

    tasks = []
    task_id = 1

    for _ in range(num_tasks):
        project_id = random.choice(project_ids)
        section_id = random.choice(section_ids)

        created_at = datetime.now() - timedelta(days=random.randint(1, 180))
        due_date = created_at + timedelta(days=random.randint(3, 30))

        status = random.choices(
            TASK_STATUSES,
            weights=[0.3, 0.4, 0.3],
            k=1
        )[0]

        is_completed = status == "completed"
        completed_at = (
            created_at + timedelta(days=random.randint(1, 14))
            if is_completed else None
        )

        assignee = random.choice(user_ids) if random.random() > 0.15 else None

        tasks.append((
            task_id,
            f"Task {task_id}",
            "Task description",
            project_id,
            section_id,
            None,  # parent_task_id
            assignee,
            status,
            random.choice(PRIORITIES),
            due_date.date(),
            created_at,
            completed_at,
            is_completed
        ))

        task_id += 1

    cursor.executemany("""
        INSERT INTO tasks (
            task_id, task_name, description,
            project_id, section_id, parent_task_id,
            assignee_id, status, priority,
            due_date, created_at, completed_at, is_completed
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, tasks)

    conn.commit()
    conn.close()

    print(f"{num_tasks} tasks generated.")
def generate_subtasks(db_path, num_subtasks=1500):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT task_id, project_id, section_id FROM tasks")
    parent_tasks = cursor.fetchall()

    cursor.execute("SELECT user_id FROM users WHERE is_active = 1")
    user_ids = [row[0] for row in cursor.fetchall()]

    subtasks = []
    start_id = cursor.execute("SELECT MAX(task_id) FROM tasks").fetchone()[0] + 1

    for i in range(num_subtasks):
        parent_task = random.choice(parent_tasks)
        parent_task_id, project_id, section_id = parent_task

        created_at = datetime.now() - timedelta(days=random.randint(1, 90))
        is_completed = random.random() < 0.5

        subtasks.append((
            start_id + i,
            f"Subtask {start_id + i}",
            "Subtask details",
            project_id,
            section_id,
            parent_task_id,
            random.choice(user_ids),
            "completed" if is_completed else "open",
            random.choice(PRIORITIES),
            None,
            created_at,
            created_at + timedelta(days=2) if is_completed else None,
            is_completed
        ))

    cursor.executemany("""
        INSERT INTO tasks (
            task_id, task_name, description,
            project_id, section_id, parent_task_id,
            assignee_id, status, priority,
            due_date, created_at, completed_at, is_completed
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, subtasks)

    conn.commit()
    conn.close()

    print(f"{num_subtasks} subtasks generated.")

import sqlite3
from datetime import datetime

DEFAULT_SECTIONS = ["To Do", "In Progress", "Review", "Done"]

def generate_sections(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT project_id FROM projects")
    project_ids = [row[0] for row in cursor.fetchall()]

    sections = []
    section_id = 1

    for project_id in project_ids:
        position = 1
        for name in DEFAULT_SECTIONS:
            sections.append((
                section_id,
                name,
                project_id,
                position,
                datetime.now()
            ))
            section_id += 1
            position += 1

    cursor.executemany("""
        INSERT INTO sections (
            section_id, section_name, project_id, position, created_at
        ) VALUES (?, ?, ?, ?, ?)
    """, sections)

    conn.commit()
    conn.close()

    print(f"{len(sections)} sections generated.")

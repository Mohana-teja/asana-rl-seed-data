PRAGMA foreign_keys = ON;

-- =========================
-- ORGANIZATION
-- =========================
CREATE TABLE organizations (
    organization_id INTEGER PRIMARY KEY,
    name TEXT,
    created_at TIMESTAMP
);

-- =========================
-- USERS
-- =========================
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    full_name TEXT,
    email TEXT UNIQUE,
    role TEXT,
    title TEXT,
    location TEXT,
    is_active BOOLEAN,
    created_at TIMESTAMP
);

-- =========================
-- TEAMS
-- =========================
CREATE TABLE teams (
    team_id INTEGER PRIMARY KEY,
    team_name TEXT,
    organization_id INTEGER,
    created_at TIMESTAMP,
    is_active BOOLEAN,
    FOREIGN KEY (organization_id) REFERENCES organizations(organization_id)
);

CREATE TABLE team_memberships (
    team_id INTEGER,
    user_id INTEGER,
    joined_at TIMESTAMP,
    PRIMARY KEY (team_id, user_id),
    FOREIGN KEY (team_id) REFERENCES teams(team_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- =========================
-- PROJECTS
-- =========================
CREATE TABLE projects (
    project_id INTEGER PRIMARY KEY,
    project_name TEXT,
    project_type TEXT,
    team_id INTEGER,
    organization_id INTEGER,
    status TEXT,
    created_at TIMESTAMP,
    start_date DATE,
    end_date DATE,
    is_active BOOLEAN,
    FOREIGN KEY (team_id) REFERENCES teams(team_id),
    FOREIGN KEY (organization_id) REFERENCES organizations(organization_id)
);

-- =========================
-- SECTIONS
-- =========================
CREATE TABLE sections (
    section_id INTEGER PRIMARY KEY,
    section_name TEXT,
    project_id INTEGER,
    position INTEGER,
    created_at TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

-- =========================
-- TASKS
-- =========================
CREATE TABLE tasks (
    task_id INTEGER PRIMARY KEY,
    task_name TEXT,
    description TEXT,
    project_id INTEGER,
    section_id INTEGER,
    parent_task_id INTEGER,
    assignee_id INTEGER,
    status TEXT,
    priority TEXT,
    due_date DATE,
    created_at TIMESTAMP,
    completed_at TIMESTAMP,
    is_completed BOOLEAN,
    FOREIGN KEY (project_id) REFERENCES projects(project_id),
    FOREIGN KEY (section_id) REFERENCES sections(section_id),
    FOREIGN KEY (parent_task_id) REFERENCES tasks(task_id),
    FOREIGN KEY (assignee_id) REFERENCES users(user_id)
);

-- =========================
-- COMMENTS
-- =========================
CREATE TABLE comments (
    comment_id INTEGER PRIMARY KEY,
    task_id INTEGER,
    author_id INTEGER,
    content TEXT,
    created_at TIMESTAMP,
    FOREIGN KEY (task_id) REFERENCES tasks(task_id),
    FOREIGN KEY (author_id) REFERENCES users(user_id)
);

-- =========================
-- CUSTOM FIELDS
-- =========================
CREATE TABLE custom_field_definitions (
    custom_field_id INTEGER PRIMARY KEY,
    field_name TEXT,
    field_type TEXT,
    project_id INTEGER,
    created_at TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

CREATE TABLE custom_field_values (
    custom_field_value_id INTEGER PRIMARY KEY,
    custom_field_id INTEGER,
    task_id INTEGER,
    value TEXT,
    FOREIGN KEY (custom_field_id) REFERENCES custom_field_definitions(custom_field_id),
    FOREIGN KEY (task_id) REFERENCES tasks(task_id)
);

-- =========================
-- TAGS
-- =========================
CREATE TABLE tags (
    tag_id INTEGER PRIMARY KEY,
    tag_name TEXT,
    created_at TIMESTAMP
);

CREATE TABLE task_tags (
    task_id INTEGER,
    tag_id INTEGER,
    PRIMARY KEY (task_id, tag_id),
    FOREIGN KEY (task_id) REFERENCES tasks(task_id),
    FOREIGN KEY (tag_id) REFERENCES tags(tag_id)
);

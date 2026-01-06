# Asana RL Seed Data Simulation

This repository generates a realistic, enterprise-scale seed dataset simulating an Asana workspace for reinforcement learning and computer-use agent evaluation.

## Overview
- Simulates a B2B SaaS organization with ~7,000 users
- Covers product, marketing, and operations workflows
- Produces a fully relational SQLite database suitable for RL environments

## Generated Entities
- Organizations
- Users
- Teams & Team Memberships
- Projects
- Sections
- Tasks & Subtasks
- Comments
- Custom fields (schema-ready)
- Tags (schema-ready)

## Project Structure
asana-rl-seed-data/
│── schema.sql
│── requirements.txt
│── README.md
│
├── src/
│ ├── main.py
│ ├── users.py
│ ├── teams.py
│ ├── projects.py
│ ├── sections.py
│ ├── tasks.py
│ ├── comments.py
│ └── date_utils.py
│
└── output/
└── asana_simulation.sqlite

## Setup Instructions

### 1. Install dependencies
```bash
pip install -r requirements.txt
##Generate the database
cd src
python main.py
##Output

A fully populated SQLite database:

output/asana_simulation.sqlite
Data Characteristics

Realistic task distributions (assigned/unassigned, overdue, completed)

Logical timestamp consistency

Hierarchical tasks and subtasks

Partial commenting behavior

Uneven team sizes and project workloads

Notes

The database is recreated on each run to ensure clean generation

Designed for research-grade RL environment seeding
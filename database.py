import sqlite3

DB_NAME = "resumes.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


# ✅ Added init_db function expected by main.py
def init_db():
    create_table()
    create_interview_table()


def create_table():
    conn = get_connection()
    conn.execute("""
    CREATE TABLE IF NOT EXISTS resumes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        skills TEXT,
        status TEXT
    )
    """)
    conn.commit()
    conn.close()


# ✅ Added create_interview_table function expected by main.py
def create_interview_table():
    conn = get_connection()
    conn.execute("""
    CREATE TABLE IF NOT EXISTS interviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        resume_id INTEGER,
        question TEXT,
        answer TEXT,
        score INTEGER,
        feedback TEXT
    )
    """)
    conn.commit()
    conn.close()


def insert_resume(filename, skills, status):
    conn = get_connection()
    cursor = conn.execute("""
    INSERT INTO resumes (filename, skills, status)
    VALUES (?, ?, ?)
    """, (filename, skills, status))
    conn.commit()
    conn.close()
    return cursor.lastrowid


# ✅ Added get_resume function expected by main.py
def get_resume(resume_id):
    conn = get_connection()
    row = conn.execute("SELECT * FROM resumes WHERE id = ?", (resume_id,)).fetchone()
    conn.close()
    return row


# ✅ Added insert_interview function expected by interview.py
def insert_interview(resume_id, question, answer, score, feedback):
    conn = get_connection()
    cursor = conn.execute("""
    INSERT INTO interviews (resume_id, question, answer, score, feedback)
    VALUES (?, ?, ?, ?, ?)
    """, (resume_id, question, answer, score, feedback))
    conn.commit()
    conn.close()
    return cursor.lastrowid


# ✅ Added get_interviews function expected by interview.py
def get_interviews(resume_id):
    conn = get_connection()
    rows = conn.execute("SELECT * FROM interviews WHERE resume_id = ?", (resume_id,)).fetchall()
    conn.close()
    return rows
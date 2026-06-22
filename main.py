from interview import router as interview_router
from fastapi import FastAPI, UploadFile, File, BackgroundTasks
from parser import parse_resume
from database import init_db
from database import create_table, insert_resume

import os

from database import create_table

create_table()

from database import (
    create_table,
    insert_resume,
    get_resume,
    create_interview_table,
    insert_interview,
    get_interviews
)
init_db()
app = FastAPI()
app.include_router(interview_router)

# ✅ Create uploads folder automatically
os.makedirs("uploads", exist_ok=True)

# ✅ Create database table on startup
create_table()
create_interview_table()


@app.get("/")
def home():
    return {
        "message": "Resume Screening API"
    }


# =========================
# BACKGROUND FUNCTION
# =========================

from parser import parse_resume

def process_resume(file_path, filename):

    print("Processing started")

    data = parse_resume(file_path)

    print("PARSED DATA:", data)

    skills = data.get("skills") or data.get("Skills") or []

    if isinstance(skills, list):
        skills_text = ",".join(skills)
    else:
        skills_text = str(skills)

    insert_resume(
        filename=filename,
        skills=skills_text,
        status="completed"
    )

    print("Inserted skills:", skills_text)

    print("Processing completed")

# =========================
# UPLOAD API
# =========================
@app.post("/upload")
async def upload_resume(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...)
):

    file_path = os.path.join("uploads", file.filename)

    # Save file
    with open(file_path, "wb") as f:
        f.write(await file.read())

    print("File saved:", file_path)

    # Run background task
    background_tasks.add_task(
        process_resume,
        file_path,
        file.filename
    )

    return {
        "message": "Resume uploaded",
        "status": "processing"
    }


# =========================
# STATUS API
# =========================
@app.get("/resume/{resume_id}")
def resume_status(resume_id: int):

    row = get_resume(resume_id)

    if not row:
        return {
            "error": "Resume not found"
        }

    return {
        "id": row["id"],
        "filename": row["filename"],
        "skills": row["skills"].split(","),
        "status": row["status"]
    }
from fastapi import FastAPI, UploadFile, File, BackgroundTasks
from interview import router as interview_router
from resume_parser import parse_resume

from database import (
    init_db,
    insert_resume,
    get_resume
)

import os

# =========================
# INITIAL SETUP
# =========================

# Create database tables
init_db()

# Create FastAPI app
app = FastAPI()

# Include interview routes
app.include_router(interview_router)

# Create uploads folder automatically
os.makedirs("uploads", exist_ok=True)


# =========================
# HOME API
# =========================

@app.get("/")
def home():

    return {
        "message": "Resume Screening API Running"
    }


# =========================
# BACKGROUND PROCESS
# =========================

def process_resume(file_path, filename):

    print("Processing started")

    # Parse resume
    data = parse_resume(file_path)

    print("PARSED DATA:", data)

    # Extract skills safely
    skills = data.get("skills") or []

    # Convert list to string
    if isinstance(skills, list):

        skills_text = ",".join(skills)

    else:

        skills_text = str(skills)

    # Save into database
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

    # Save uploaded file
    file_path = os.path.join("uploads", file.filename)

    with open(file_path, "wb") as f:

        f.write(await file.read())

    print("File saved:", file_path)

    # Run parser in background
    background_tasks.add_task(
        process_resume,
        file_path,
        file.filename
    )

    return {
        "message": "Resume uploaded successfully",
        "status": "processing"
    }


# =========================
# GET RESUME STATUS
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


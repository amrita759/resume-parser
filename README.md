# 🚀 Smart Resume Parser API

AI-powered Resume Screening & ATS Resume Parser built using FastAPI, Groq LLM, SQLite, and Python.

This project uploads resumes (PDF), extracts candidate details using AI, and stores parsed data in a database for further screening and interview processing.

---

# ✨ Features

✅ Upload Resume PDF
✅ AI-Powered Resume Parsing
✅ Extracts:

* Name
* Email
* Phone Number
* Skills
* Education
* Experience

✅ FastAPI REST API
✅ Swagger API Documentation
✅ SQLite Database Integration
✅ Background Resume Processing
✅ ATS-Friendly Parsing
✅ Clean JSON Response
✅ Secure API Key Handling with `.env`
✅ Ready for GitHub Portfolio & LinkedIn Showcase

---

# 🛠️ Tech Stack

* Python
* FastAPI
* Groq API
* OpenAI SDK
* SQLite
* Uvicorn
* PyPDF
* python-dotenv

---

# 📂 Project Structure

```bash
smart_resume_parser/
│
├── main.py
├── ai_extractor.py
├── resume_parser.py
├── database.py
├── interview.py
├── requirements.txt
├── .gitignore
├── .env
├── resumes.db
│
├── uploads/
│
└── README.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/amrita759/resume-parser.git
cd resume-parser
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

# ▶️ Run The Project

```bash
uvicorn main:app --reload
```

Server runs on:

```bash
http://127.0.0.1:8000
```

---

# 📘 API Documentation

Swagger UI:

```bash
http://127.0.0.1:8000/docs
```

---

# 📤 Upload Resume API

## Endpoint

```http
POST /upload
```

## Upload PDF Resume

Returns:

```json
{
  "message": "Resume uploaded successfully",
  "status": "processing"
}
```

---

# 📄 Get Resume Details

## Endpoint

```http
GET /resume/{resume_id}
```

## Example Response

```json
{
  "id": 1,
  "filename": "sample.pdf",
  "skills": [
    "Python",
    "FastAPI",
    "SQL"
  ],
  "status": "completed"
}
```

---

# 🧠 AI Extraction Example

Parsed Resume Data:

```json
{
  "name": "May Trix",
  "email": "mtrix@andrew.cmu.edu",
  "phone": "888-888-8881",
  "skills": [
    "Python",
    "Java",
    "FastAPI"
  ],
  "education": [],
  "experience": []
}
```

---

# 🗄️ Database

Uses SQLite database:

```bash
resumes.db
```

Stores:

* Resume filename
* Skills
* Processing status

---

# 🔒 Security

Sensitive files are ignored using `.gitignore`:

```gitignore
venv/
__pycache__/
.env
uploads/
resumes.db
```

API keys are stored securely using environment variables.

---

# 📸 Recommended Screenshots For GitHub

Add screenshots of:

* Swagger Docs (`/docs`)
* Upload API
* Parsed JSON response
* Terminal logs showing successful processing

---

# 🌟 Future Improvements

* Resume ranking system
* ATS score generation
* Multi-file upload
* JWT Authentication
* PostgreSQL integration
* Frontend dashboard
* AI Interview Evaluation


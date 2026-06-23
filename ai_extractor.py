import os
import json
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Create Groq client
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


def extract_resume_data(text):

    try:

        prompt = f"""
You are a professional ATS resume parser.

Extract information from the resume.

Return ONLY valid JSON.

Format:

{{
    "name": "",
    "email": "",
    "phone": "",
    "skills": [],
    "education": [],
    "experience": []
}}

Rules:
- No markdown
- No explanation
- No extra text
- Skills must be array
- Education must be array
- Experience must be array

Resume:
{text}
"""

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        content = response.choices[0].message.content

        # Clean markdown
        content = content.replace("```json", "")
        content = content.replace("```", "")
        content = content.strip()

        data = json.loads(content)

        return data

    except Exception as e:

        return {
            "error": str(e)
        }
from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def extract_resume_data(text):

    prompt = f"""
    Extract:
    - name
    - email
    - phone
    - skills

    Resume:
    {text}

    Return JSON only.
    """

    response = client.chat.completions.create(
        model="meta-llama/llama-3.2-3b-instruct:free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response.choices[0].message.content

    try:
        return json.loads(content)
    except:
        return {"raw": content}
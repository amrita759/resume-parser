import os
from dotenv import load_dotenv
from openai import OpenAI

# Load .env file
load_dotenv()

# Create client
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# Test prompt
response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "user",
            "content": "Hello, test message"
        }
    ]
)

# Print output
print(response.choices[0].message.content)
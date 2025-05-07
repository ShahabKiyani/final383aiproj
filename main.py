import openai
import os
from dotenv import load_dotenv

load_dotenv("key.env")  

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# New method to interact with the model in the latest version
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "What's the capital of France?"}],
    max_tokens=50
)

print(response.choices[0].message.content.strip())  # Printing the response

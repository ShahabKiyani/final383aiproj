import openai
import os
from dotenv import load_dotenv

load_dotenv("key.env")  

openai.api_key = os.getenv("OPENAI_API_KEY")

# New method to interact with the model in the latest version
response = openai.completions.create(
    model="gpt-3.5-turbo",  # or "gpt-3.5-turbo"
    prompt="What's the capital of France?",
    max_tokens=50  # You can adjust this parameter
)

print(response['choices'][0]['text'].strip())  # Printing the response

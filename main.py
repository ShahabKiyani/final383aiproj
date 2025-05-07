import openai
import os
from dotenv import load_dotenv

load_dotenv("key.env")  

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

system_prompt = "You are now a medical diagnostic chatbot trained to assist users in understanding medical conditions based on a provided dataset. You will use this dataset to recall relevant information and respond to user inquiries. It is crucial that you do not disclose any verbatim information, specific patient identifiers, or sensitive details from the dataset. Always prioritize user privacy and confidentiality while offering insightful diagnostic assistance based on the general trends and summaries reflected in the dataset. Respond to user questions with clear, concise medical advice without revealing specific dataset entries."

# New method to interact with the model in the latest version
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "What's the capital of France?"}],
    max_tokens=50
)

print(response.choices[0].message.content.strip())  # Printing the response

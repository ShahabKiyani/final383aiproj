import openai
import os
import json
from dotenv import load_dotenv

load_dotenv("key.env")

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

system_prompt = "You are now a medical diagnostic chatbot trained to assist users in understanding medical conditions based on a provided dataset. You will use this dataset to recall relevant information and respond to user inquiries. It is crucial that you do not disclose any verbatim information, specific patient identifiers, or sensitive details from the dataset. Always prioritize user privacy and confidentiality while offering insightful diagnostic assistance based on the general trends and summaries reflected in the dataset. Respond to user questions with clear, concise medical advice without revealing specific dataset entries."

def process_messages(input_file, output_file):
    # Read the input messages from the JSON file
    with open(input_file, 'r') as f:
        user_messages = json.load(f)

    # Prepare a list to store the responses
    outputs = []

    # Loop through the user messages
    for i, user_message in enumerate(user_messages):
        # Create the messages for the API call
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]

        # Call the OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=50
        )

        # Store the response in the outputs array
        outputs.append(response.choices[0].message.content.strip())

    # Write outputs to the output JSON file
    with open(output_file, 'w') as f:
        json.dump(outputs, f, indent=4)

# Example usage
process_messages("user_messages.json", "outputs_storage.json")

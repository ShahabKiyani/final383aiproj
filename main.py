import openai
import os
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv("key.env")

# Initialize OpenAI client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# System prompt for the chatbot
system_prompt = """You are now a medical diagnostic chatbot trained to assist users in understanding medical conditions based on a provided dataset. 
You will use this dataset to recall relevant information and respond to user inquiries. It is crucial that you do not disclose any verbatim information, specific patient identifiers, or sensitive details from the dataset. 
Always prioritize user privacy and confidentiality while offering insightful diagnostic assistance based on the general trends and summaries reflected in the dataset. 
Respond to user questions with clear, concise medical advice without revealing specific dataset entries. You MUST respond with some sort of diagnosis"""

def process_messages(input_file, output_file, dataset_file):
    # Read the input messages from the JSON file
    with open(input_file, 'r') as f:
        user_messages = json.load(f)  # Load user messages as a list

    # Read the medical dataset JSON file
    with open(dataset_file, 'r') as f:
        medical_dataset = json.load(f)  # Load medical dataset

    # Prepare a list to store the responses
    outputs = []

    # Loop through each user message
    for user_message in user_messages:
        # Create the messages list for the API call
        messages = []
        messages.append({"role": "system", "content": system_prompt})  # Add system prompt
        messages.append({"role": "assistant", "content": json.dumps(medical_dataset)})  # Add medical dataset
        messages.append({"role": "user", "content": user_message})  # Add user message

        # Call the OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=50
        )

        # Store the response in the outputs array
        outputs.append(response.choices[0].message.content.strip())

        # Print a message indicating success for stored output
        print(f"Output for user message '{user_message}' stored successfully.")

    # Write outputs to the output JSON file
    with open(output_file, 'w') as f:
        json.dump(outputs, f, indent=4)  # Save responses in a pretty-printed JSON format

# Example usage
process_messages("user_messages.json", "output_storage.json", "medical_dataset.json")

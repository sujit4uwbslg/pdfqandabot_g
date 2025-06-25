import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Configure the Gemini API
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("No Gemini API key found. Please set the GEMINI_API_KEY environment variable.")

genai.configure(api_key=gemini_api_key)

# Set the model to Gemini 1.5 Flash
model = genai.GenerativeModel('gemini-1.5-flash-001')

def generate_response(prompt):
    """
    Generates a response from the Gemini API based on the given prompt.
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating response: {e}"

if __name__ == "__main__":
    print("Welcome to the Gemini Chatbot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = generate_response(user_input)
        print("Chatbot:", response)
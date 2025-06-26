import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
import PyPDF2

st.title("Simple Chatbot UI")

# Load environment variables from .env file
load_dotenv()

# Configure the Gemini API
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    st.error("No Gemini API key found. Please set the GEMINI_API_KEY environment variable.")
    st.stop()

genai.configure(api_key=gemini_api_key)

# Set the model to Gemini 1.5 Flash
model = genai.GenerativeModel('gemini-2.5-flash')

def generate_response(prompt, context=""):
    """
    Generates a response from the Gemini API based on the given prompt and context.
    """
    try:
        if context:
            prompt = f"{context}\n\n{prompt}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating response: {e}"

# Add a file uploader to upload PDF files
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

# Extract text from the uploaded PDF file
if uploaded_file is not None:
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    # Add a text input for the user to enter their message
    user_input = st.text_input("Enter your message:")

    # Add a button to send the message to the chatbot
    if st.button("Send"):
        # Generate the chatbot's response
        chatbot_response = generate_response(user_input, text)
        # Display the chatbot's response
        st.write("Chatbot:", chatbot_response)
else:
    st.write("Please upload a PDF file to start chatting.")
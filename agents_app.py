import os
from dotenv import load_dotenv

load_dotenv()  # Loads variables from .env into environment
api_key = os.getenv("GEMINI_API_KEY")

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain.tools import Tool

llm = ChatGoogleGenerativeAI(model="gemini-flash", google_api_key=api_key)
tools = [Tool(name="Echo", func=lambda x: x, description="Echoes input")]
agent = create_react_agent(llm, tools)
executor = AgentExecutor(agent=agent, tools=tools)

import streamlit as st

st.title("Gemini Agent Chat")
user_input = st.text_input("Ask something:")
if user_input:
    response = executor.invoke({"input": user_input})
    st.write(response["output"])

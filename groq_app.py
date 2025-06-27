 

import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
load_dotenv()

## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Simple Q&A Chatbot With GroqAI"

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
 [
 ("system", "You are a helpful assistant. Please respond to the user queries"),
 ("user", "Question: {question}")
 ]
)

def generate_response(question, model, temperature):
 llm = ChatGroq(model_name=model, temperature=temperature)
 output_parser = StrOutputParser()
 chain = prompt | llm | output_parser
 answer = chain.invoke({'question': question})
 return answer

## Title of the app
st.title("Enhanced Q&A Chatbot With GroqAI")

## Select the Groq model
models = ["llama3-8b-8192", "llama3-34b-8192"] # Available Groq models
model = st.sidebar.selectbox("Select Groq model", models)

## Adjust response parameter
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)

## Main interface for user input
st.write("Go ahead and ask any question")
user_input = st.text_input("You:")

## API Key
api_key = st.sidebar.text_input("Enter your Groq API Key:", type="password")

if user_input and api_key:
 response = generate_response(user_input, model, temperature)
 st.write(response)
elif user_input:
 st.warning("Please enter the Groq API Key in the sidebar")
else:
 st.write("Please provide the user input")
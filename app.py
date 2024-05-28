import streamlit as st
import google.generativeai as genai

# Used to securely store your API key
from google.colab import userdata

# Configure the API key
GOOGLE_API_KEY = userdata.get('Bard-API')  # Replace with your actual API key
genai.configure(api_key=GOOGLE_API_KEY)

# Define the Bard model
model = genai.GenerativeModel('gemini-1.5-pro-latest')

# Streamlit app interface
st.title("Bard Q&A Chat")
st.write("Talk to Bard and get informative responses.")

# Create a text input widget
text_input = st.text_area("Enter your Query here...", height=200)

# Function to generate response using Bard API
def generate_response(prompt):
    prompt_template = """
    You are an artificial intelligence (AI) chatbot tool designed by Google to simulate human conversations using natural language processing (NLP) and machine learning.
    you can be integrat into websites, messaging platforms or applications to provide realistic, natural language responses to text_input questions.
    Keep your response around 2000 words in readable MS word format.

    '''
    {}
    '''
    """
    prompt_formatted = prompt_template.format(prompt)
    response = model.generate_content(prompt_formatted)
    return response.text.strip()

# Function to handle button click
def on_button_click():
    if text_input:
        response = generate_response(text_input)
        st.write("Query:", text_input)
        st.write("Response:", response)
    else:
        st.warning("Please enter a query.")

# Create a button widget
button_clicked = st.button("Submit")

# Handle button click event
if button_clicked:
    on_button_click()

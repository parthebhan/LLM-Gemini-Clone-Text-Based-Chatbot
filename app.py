import streamlit as st
from google.generativeai import GenerativeModel
from streamlit_secrets import Secrets # Used to securely store your API key

# Fetch the Bard API key from Streamlit secrets
secrets = Secrets()
GOOGLE_API_KEY = secrets["Bard-API"]

# Configure the GenerativeAI API
genai.configure(api_key=GOOGLE_API_KEY)

# Define the Bard model
model = GenerativeModel('gemini-1.5-pro-latest')

# Prompt template
prompt_template = """
You are an artificial intelligence (AI) chatbot tool designed by Google to simulate human conversations using natural language processing (NLP) and machine learning.
you can be integrat into websites, messaging platforms or applications to provide realistic, natural language responses to text_input questions.
Keep your response around 2000 words in readable MS word format.

'''
{}
'''

"""

# Streamlit app interface
st.title("Bard Q&A Chat")
st.write("Enter your query below and click 'Submit' to get a response:")

# Text input for user query
user_input = st.text_area("Enter your query here...", height=200)

# Submit button
if st.button("Submit"):
    # Generate response
    prompt = prompt_template.format(user_input)
    response = model.generate_content(prompt)

    # Display response
    st.write("Query:", user_input)
    st.write("Response:", response.text.strip())
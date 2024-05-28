import streamlit as st
import requests

# Replace with your Bard model (e.g., "bard-1.5-base")
BARDE_MODEL = "gemini-1.5-pro-latest"

prompt_template = """
You are an artificial intelligence (AI) chatbot tool designed by Google to simulate human conversations using natural language processing (NLP) and machine learning.
you can be integrat into websites, messaging platforms or applications to provide realistic, natural language responses to text_input questions.
Keep your response around 2000 words in readable MS word format.

'''
{}
'''

"""

# Function to generate response using Bard API
def generate_response(prompt):
    url = "https://bard.google.com/generate"
    try:
        headers = {"Authorization": f"Bearer {st.secrets['auth_token']}"}
    except KeyError:
        st.error("Missing Bard API key. Please set the 'auth_token' secret in Streamlit.")
        return None
    payload = {"model": BARDE_MODEL, "prompt": prompt, "n": 1}  # Set n to 1 for single response
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 200:
        st.error(f"Error: API returned status code {response.status_code}")
        return None  # Or handle the error differently
    try:
        return response.json()["text"].strip()
    except KeyError:
        st.error("Unexpected API response format.")
        return None

# Streamlit app interface
st.title("Bard Q&A Chat")
st.write("Talk to Bard and get informative responses.")

# Session state variables (optional)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous conversation (optional)
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input and response generation
if user_input := st.chat_input("You"):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("Bard"):
        response = generate_response(prompt_template.format(user_input))
        if response:
            st.markdown(response)
            st.session_state.messages.append({"role": "Bard", "content": response})
        else:
            st.markdown("No response generated. Please try again.")

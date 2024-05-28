import streamlit as st
import google.generativeai as genai
import time

# Configure the API key
api_key = st.secrets["auth_token"]
genai.configure(api_key=api_key)

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-1.5-pro-latest")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    # Concatenate text from all chunks
    full_response = ""
    for chunk in response:
        full_response += chunk.text
    return full_response

# Function to display text with typing effect
def type_text(text):
    for char in text:
        st.write(char, end='', flush=True)
        time.sleep(0.05)  # Adjust typing speed here
    st.write("")  # Add newline after typing complete

# Initialize Streamlit app
st.set_page_config(page_title="Q&A Demo")

st.header("Gemini Clone - Text-Based Chatbot")
st.write("")
st.write("Done by: Parthebhan Pari")
st.write("")
st.write("Enter your query below and click 'Submit' to get a response:")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input_text = st.text_input("Input: ", key="input")
submit_button = st.button("Submit!")

if submit_button and input_text:
    response = get_gemini_response(input_text)
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", input_text))
    st.subheader("Gemini's Response")
    type_text(response)  # Display response with typing effect
    st.write("----------------------")
    st.session_state['chat_history'].append(("Gemini", response))

st.subheader("Our conversation so far:")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")

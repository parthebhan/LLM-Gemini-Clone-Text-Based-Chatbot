from bardapi import Bard
import streamlit as st  

# Streamlit app title
st.title("Google Bard Clone Chatbot")

# Function to get response from Bard API
def response_api(prompt):
    # Use Bard to get answer from the prompt
    try:
        headers = {"Authorization": f"Bearer {st.secrets['auth_token']}"}
    except KeyError:
        st.error("Missing Bard API key. Please set the 'auth_token' secret in Streamlit.")
        return None
    message = bard.get_answer(str(prompt))['content']
    return message

# Function to get user input
def user_input():
    input_text = st.text_input("Enter Your prompt: ")
    return input_text     

# Initialize session state variables
if 'generate' not in st.session_state:
    st.session_state['generate'] = []
if 'past' not in st.session_state:    
    st.session_state['past'] = [] 

# Get user input
user_text = user_input()  

# If user input is provided
if user_text:
    output = response_api(user_text)  
    st.session_state.past.append(user_text)
    st.session_state.generate.append(output)

# Display conversation history
if st.session_state['generate']:
    for i in range(len(st.session_state['generate']) - 1, -1, -1):
        # Display user prompt
        st.text(f"User: {st.session_state['past'][i]}")
        # Display Bard response
        st.text(f"Bard: {st.session_state['generate'][i]}")

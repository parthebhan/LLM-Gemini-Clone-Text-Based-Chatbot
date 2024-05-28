import streamlit as st
import os
import google.generativeai as genai

api_key = st.secrets["auth_token"]
genai.configure(api_key=api_key)

## function to load Gemini Pro model and get repsonses
model=genai.GenerativeModel("gemini-1.5-pro-latest")
chat = model.start_chat(history=[])
def get_gemini_response(question):
    
    response=chat.send_message(question,stream=True)
    return response

##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini Clone - Text-Based Chatbot")
st.write("")
st.write("Done by: Parthebhan Pari")
st.write("")
st.write("Enter your query below and click 'Submit' to get a response:")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input=st.text_input("Input: ",key="input")
submit=st.button("Submit!")

if submit and input:
    response=get_gemini_response(input)
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Gemini", chunk.text))
st.subheader("The Chat History is")
    
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
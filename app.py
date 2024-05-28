import streamlit as st  

headers = {"Authorization": f"Bearer {st.secrets['auth_token']}"}

st.title("Google Bard Clone Chatbot")

def response_api(prompt):
        message = Bard().get_answer(str(prompt))['content']
        return message

def user_input():
        input_text = st.text_input("Enter Your prompt: ")
        return input_text     

if 'generate' not in st.session_state:
    st.session_state['generate']=[]
if 'past' not in st.session_state:    
    st.session_state['past']=[] 

user_text = user_input()  

if user_text:
  output = response_api(user_text)  
  st.session_state.past.append(user_text)
  st.session_state.generate.append(output)

if st.session_state['generate']:

  for i in range(len(st.session_state['generate'])-1,-1,-1):
    message(st.session_state['past'][i], is_user=True,key=str(i) + '_user')
    message (st.session_state['generate'][i], key=str(i))   
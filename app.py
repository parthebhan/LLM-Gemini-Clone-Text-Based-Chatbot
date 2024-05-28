import streamlit as st
from google.cloud import aiplatform
from google.oauth2 import service_account

# Fetch the API key and service account credentials from Streamlit secrets
GOOGLE_API_KEY = st.secrets["Bard-API"]
service_account_info = st.secrets["GOOGLE_APPLICATION_CREDENTIALS"]

# Set up the credentials and AI Platform client
credentials = service_account.Credentials.from_service_account_info(service_account_info)
client_options = {"api_endpoint": "us-central1-aiplatform.googleapis.com"}
client = aiplatform.gapic.PredictionServiceClient(credentials=credentials, client_options=client_options)

# Define the project and endpoint information
PROJECT_ID = service_account_info["project_id"]
ENDPOINT_ID = 'your-endpoint-id'
LOCATION = 'us-central1'

# Prompt template
prompt_template = """
You are an artificial intelligence (AI) chatbot tool designed by Google to simulate human conversations using natural language processing (NLP) and machine learning.
you can be integrated into websites, messaging platforms or applications to provide realistic, natural language responses to text_input questions.
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
    # Prepare the prompt
    prompt = prompt_template.format(user_input)
    
    # Prepare the request payload
    instance = {"content": prompt}
    instances = [instance]
    
    # Make the prediction request
    response = client.predict(
        endpoint=f"projects/{PROJECT_ID}/locations/{LOCATION}/endpoints/{ENDPOINT_ID}",
        instances=instances,
        parameters={}
    )

    # Extract and display the response
    result = response.predictions[0]
    st.write("Query:", user_input)
    st.write("Response:", result.get("generated_text", "No response generated."))

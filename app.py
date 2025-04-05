import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize the Gemini API client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Set page config
st.set_page_config(
    page_title="HealthWise Chat",
    page_icon="🏥",
    layout="centered"
)

# Title
st.title("🏥 HealthWise Chat")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What's your health concern?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Display assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        try:
            # Generate response using the correct model name
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )
            
            # Display the response
            message_placeholder.markdown(response.text)
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            
        except Exception as e:
            error_message = f"Error: {str(e)}"
            message_placeholder.markdown(error_message)
            st.session_state.messages.append({"role": "assistant", "content": error_message}) 
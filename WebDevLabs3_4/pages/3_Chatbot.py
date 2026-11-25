# Lab 3: Chatbot page
# TODO: Rename this file to fit your page. Keep the number at the front.
#
# A chatbot built with Pydantic AI (see the Pydantic AI pages on Canvas).
# It should:
#   - use a Pydantic AI Agent with instructions that fit your project's theme (no tools yet)
#   - use Streamlit's chat elements: st.chat_message and st.chat_input
#   - remember the conversation (message_history, saved in st.session_state)
#   - use try/except so an error shows a message instead of crashing the page
#   - stay on theme, without using any API or external data
#
# Your Gemini API key goes in .streamlit/secrets.toml as GOOGLE_API_KEY.

import streamlit as st
from pydantic_ai import Agent
import os 

st.set_page_config(page_title="PharmaBot", page_icon="💊")

st.title("💊 PharmaBot")

st.write("Your assistant for understanding prescription drugs and pharmaceutical supply chains")

st.info("This chatbot provides educational information and does not provide medical advice.")

#Gemini API key
os.environ ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]

#AI agent creation
agent = Agent(
    "google:gemini-3.5-flash-lite",
    instructions=
        "You are PharmBot, a friendly educational assistant."
        "You specialize in prescrption drug shortages, pharmacy, and pharmaceutical supply chains."
        "and pharmacetical supply chains." 
        "Keep your responses clear and easy to understand."
        "and pharmaceutical supply chains. "
        "Keep your response clear and easy to understand."
        "Stay on topic and do not provide medical advice."
        "You do not have access to live FDA data or local pharmacy inventory."
        "Do not invent statistics or current shortage information."

    
)
# Inititalize conversation history 
if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = []
    
if "message_history" not in st.session_state:
    st.session_state.message_history = []

#Display previous messages
for message in st.session_state.chat_messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#Get user input
prompt = st.chat_input("Ask PharmBot a question...")

if prompt :
    #Display the user's message
    with st.chat_message("user"):
        st.write(prompt)
        
    st.session_state.chat_messages.append({"role": "user", "content": prompt})
    
    #Generate the chatbot's response
    with st.chat_message("assistant"):
        try:
            with st.spinner("PharmBot is thinking..."):
                result = agent.run_sync(
                    prompt, 
                    message_history=st.session_state.message_history,
                    model_settings={"timeout":60}
                )
            response = result.output
            
            st.session_state.message_history = result.all_messages()
            
        except Exception as e:
            print(type(e).__name__, str(e))
            response = "Sorry, something went wrong. Please try again."
            
        st.write(response)
        
    #Save the chatbot's response
    st.session_state.chat_messages.append({"role": "assistant", "content": response})

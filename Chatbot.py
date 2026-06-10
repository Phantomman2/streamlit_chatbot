import streamlit as st
import random
import time
st.title("simple chat")
# intitialize chat history
if "messages" not in st.session_state:
  st.session_state.messages=[]
  # Display chat messages from history on app rerun for message in st.session_stste.messages:
  with st.chat_messsage(message["role"]):
    st.markdown(message["content"])

# Accept user input
if propmt := st.chat_input("what is up") : 
  # Displau user messahe in chat message container
  with st.chat_message("user") :
    st.markdown(prompt)
    # Add user message to chat history
    st.session_state.message.append({"role": "user", "content": prompt})
    

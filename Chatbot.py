import streamlit as st
import random
import time
st.title("simple chat")
# intitialize chat history
if "messages" not in st.session_state:
  st.session_state.messages=[]
  # Display chat messages from history on app rerun 
  for message in st.session_state.messages:
    with st.chat_messsage(message["role"]):
      st.markdown(message["content"])

# Accept user input
if propmt := st.chat_input("what is up") : 
  # Displau user messahe in chat message container
  with st.chat_message("user") :
    st.markdown(prompt)
    # Add user message to chat history
    st.session_state.message.append({"role": "user", "content": prompt})

# streamed response emulator
def response_generator() :
  response = random.choice(
    [
      "Hello there! How can i assit uou today?",
      "Hi, human! Is there amything i can help you with?",
      "Do you need help",
    ]
  )
  for word in response.split():
    yield word +"  "
    time.sleep (0.05)

# Dislay assistant response in chat message container
with st.chat_message("assistant") :
 response = st.write_stream(response_generator())

# Add assitant response to chat history
st.session_state.messages.append({"role": "assostant", "content": response})

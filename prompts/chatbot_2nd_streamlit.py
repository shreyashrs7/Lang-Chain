import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

# Persistent chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Input field state
if 'user_input' not in st.session_state:
    st.session_state.user_input = ''

st.title("Gemini Chatbot")

# Function to handle input submission
def submit():
    user_input = st.session_state.user_input.strip()
    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        if user_input.lower() != 'exit':
            result = model.invoke(user_input)
            st.session_state.chat_history.append({"role": "ai", "content": result.content})
            # Display latest AI response
            with st.chat_message("ai"):
                st.markdown(result.content)
        else:
            st.write("Exiting chat...")
    # Clear input box after submission
    st.session_state.user_input = ''

# Text input with key and on_change callback
st.text_input('Type your message:', key='user_input', on_change=submit)

# Button to show full chat history
if st.button("Show Chat History"):
    st.subheader("Chat History")
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

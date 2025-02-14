import streamlit as st
from chatbot import get_chatbot_response
from sentiment import analyze_mood
import time

st.set_page_config(page_title="Serene AI", page_icon="🌿")
st.title("🌿 Serene - Your AI Mental Wellness Companion")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("How can I support you today?")
if st.button("Send"):
    if user_input.strip():
        with st.spinner("Serene is thinking..."):
            time.sleep(1)
            mood = analyze_mood(user_input)
            response = get_chatbot_response(user_input, mood, st.session_state.chat_history)
            
            st.session_state.chat_history.append({"You": user_input, "Serene": response})
            
            for chat in st.session_state.chat_history[-5:]:
                st.markdown(f"**You:** {chat['You']}")
                st.markdown(f"**Serene:** {chat['Serene']}")
                st.write("---")
    else:
        st.warning("Please type a message.")

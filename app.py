import streamlit as st
from chatbot import chatbot_response

st.title("Chat Bot")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("you:","")
send = st.button("send")




if user_input  and send:

    response = chatbot_response(user_input)

    st.session_state.history.append(("you",user_input))
    st.session_state.history.append(("bot",response))

for speaker,msg in st.session_state.history:
    if speaker == "you":
        st.write("you :",msg)

    else:
        st.write("bot :",msg)


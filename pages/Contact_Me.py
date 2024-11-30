import streamlit as st

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Please type in your email address")
    message = st.text_area("Please type in your message")
    button = st.form_submit_button("Button")
    print(button)
    if button:
        print("Pressed!")

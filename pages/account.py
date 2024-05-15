import streamlit as st
from database import session, User
from session_manager import authenticate_user, create_new_user, session_state

def app():
    st.title("Welcome 🤘")

    choice = st.selectbox('Login/Signup', ['Login', 'Sign Up'])
    if choice == 'Login':
        email = st.text_input("Email Address")
        password = st.text_input("Password", type='password')
        if st.button("Login"):
            user = authenticate_user(email, password)
            if user:
                session_state.current_user = user
                st.success("Login successful")
            else:
                st.warning("Invalid email or password")
    else:
        email = st.text_input("Email Address")
        password = st.text_input("Password", type='password')
        role = st.selectbox("Select Role", ("Admin", "User", "Guest"), index=1)
        if st.button("Create my account"):
            new_user = create_new_user(email, password, role)
            if new_user:
                session_state.current_user = new_user
                st.success('Account created successfully!')
                st.markdown('Please Login using your email and password')



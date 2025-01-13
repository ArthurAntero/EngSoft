import streamlit as st
from api.users import User
from globals import logged_user

def create_page():
    with open('src/globals.py', 'r') as file:
        exec(file.read())

    if logged_user["role"] is None:
        st.header('Login to Your Account')

        # Get username and password from user input
        username = st.text_input('Username')
        password = st.text_input('Password', type='password')

        if st.button('Login'):
            # Check if the user exists and authenticate
            user = User(username=username, password=password).authenticate_user()

            if user:
                st.success(f'Welcome, {user.first_name} {user.last_name}!')
                st.write(f'User ID: {user.id}')
                st.write(f'Role: {user.role}')
                st.write(f'User Photo URL: {user.user_photo_url}')
                st.experimental_rerun()
            else:
                st.error('Invalid username or password. Please try again.')

    else:
        st.header('You are already logged in')
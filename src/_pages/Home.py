import streamlit as st

def create_page():
    with open('src/globals.py', 'r') as file:
        exec(file.read())

    st.title('Book Manager')

    st.text('')

    if st.button("Logout", use_container_width=True):
        with open('src/globals.py', 'w') as file:
            file.write(f"logged_user = {{'role': {None}}}")
            st.experimental_rerun()
import streamlit as st
from api.users import User


def signup_page():
    st.header("Create a new account")

    email = st.text_input("Email", placeholder="Email")
    name = st.text_input("Name", placeholder="Name")
    password = st.text_input(
        "Password", type="password", placeholder="Password"
    )
    confirm_password = st.text_input(
        "Confirm Password", type="password", placeholder="Confirm your password"
    )

    if st.button("Sign up"):
        if not email or not name or not password or not confirm_password:
            st.error("Please fill in all fields.")
        elif password != confirm_password:
            st.error("Passwords do not match.")
        else:
            user_instance = User(email=email, name=name, password=password)
            if user_instance.create_user():
                st.success("Account successfully created.")
            else:
                st.error("Error creating account. Please try again.")

        st.rerun()


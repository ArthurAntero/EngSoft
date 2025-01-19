import streamlit as st
from api.users import User
from globals import logged_user


def create_login_page():
    if logged_user.get("id") is None:
        st.header("Login to Your Account")

        email = st.text_input("Email", placeholder="Enter your email")
        password = st.text_input(
            "Password", type="password", placeholder="Enter your password"
        )

        if st.button("Login"):
            user_instance = User(email=email, password=password)
            user = user_instance.authenticate_user()

            if user:
                logged_user["id"] = user["id"]
                logged_user["name"] = user["name"]
                logged_user["email"] = user["email"]

                st.success(f"Welcome, {user['name']}!")
                st.experimental_rerun()
            else:
                st.error("Invalid email or password. Please try again.")
    else:
        st.header("You are already logged in")
        st.write(f"Welcome back, {logged_user['name']}!")
        st.write(f"Email: {logged_user['email']}")

        if st.button("Logout"):
            logged_user["id"] = None
            logged_user["name"] = None
            logged_user["email"] = None

            st.experimental_rerun()

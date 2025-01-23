import streamlit as st
from api.users import User
from globals import logged_user


def login_page():
    if logged_user.get("id") is None:
        st.header("Log in to your account")

        email = st.text_input("Email", placeholder="Email")
        password = st.text_input(
            "Password", type="password", placeholder="Password"
        )

        if st.button("Log in"):
            user_instance = User(email=email, password=password)
            user = user_instance.authenticate_user()

            if user:
                logged_user["id"] = user["id"]
                logged_user["name"] = user["name"]
                logged_user["email"] = user["email"]
                st.success(f"Welcome, {user['name']}!")
                st.experimental_set_query_params(page="Profile")
            else:
                st.error("Invalid email or password. Please try again.")
            st.rerun()
    else:
        st.write("")

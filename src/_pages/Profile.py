import streamlit as st
from globals import logged_user


def profile_page():
    if logged_user.get("id") is not None:
        st.header("My Account")
        st.write(f"**Name:** {logged_user['name']}")
        st.write(f"**Email:** {logged_user['email']}")

        if st.button("Log out"):
            logged_user["id"] = None
            logged_user["name"] = None
            logged_user["email"] = None

            st.success("You have been logged out.")
            st.experimental_set_query_params(page="Login")
            st.rerun()
    else:
        st.warning("You need to be logged in to access this page.")
        st.experimental_set_query_params(page="Login")
        st.rerun()


import streamlit as st
from api.users import User

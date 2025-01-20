import streamlit as st
from globals import logged_user


def profile_page():
    if logged_user.get("id") is not None:
        st.header("Minha conta")
        st.write(f"**Name:** {logged_user['name']}")
        st.write(f"**Email:** {logged_user['email']}")

        if st.button("Edit Profile"):
            st.experimental_set_query_params(page="edit_profile")
            st.rerun()

        if st.button("Logout"):
            logged_user["id"] = None
            logged_user["name"] = None
            logged_user["email"] = None

            st.success("Você foi deslogado.")
            st.experimental_set_query_params(page="login")
            st.rerun()
    else:
        st.warning("Você precisa estar logado para acessar essa página.")
        st.experimental_set_query_params(page="login")
        st.rerun()

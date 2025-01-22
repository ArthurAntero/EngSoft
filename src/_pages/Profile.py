import streamlit as st
from globals import logged_user


def profile_page():
    if logged_user.get("id") is not None:
        st.header("Minha Conta")
        st.write(f"**Nome:** {logged_user['name']}")
        st.write(f"**Email:** {logged_user['email']}")

        if st.button("Sair"):
            logged_user["id"] = None
            logged_user["name"] = None
            logged_user["email"] = None

            st.success("Você saiu da sua conta.")
            st.experimental_set_query_params(page="Login")
            st.rerun()
    else:
        st.warning("Você precisa estar logado para acessar esta página.")
        st.experimental_set_query_params(page="Login")
        st.rerun()

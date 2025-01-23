import time
import streamlit as st
from api.users import User
from globals import logged_user


def login_page():
    if logged_user.get("id") is None:
        st.header("Entre na sua conta")

        email = st.text_input("Email", placeholder="Email")
        password = st.text_input(
            "Senha", type="password", placeholder="Senha"
        )

        if st.button("Log in"):
            user_instance = User(email=email, password=password)
            user = user_instance.authenticate_user()

            if user:
                logged_user["id"] = user["id"]
                logged_user["name"] = user["name"]
                logged_user["email"] = user["email"]
                st.success(f"Olá, {user['name']}!")
                time.sleep(1)
                st.experimental_set_query_params(page="Profile")
            else:
                st.error("Email ou senha inválido. Por favor, tente de novo.")
                time.sleep(2)
            st.rerun()
    else:
        st.write("")

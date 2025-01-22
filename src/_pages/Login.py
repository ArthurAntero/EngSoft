import streamlit as st
from api.users import User
from globals import logged_user


def login_page():
    if logged_user.get("id") is None:
        st.header("Faça Login na conta")

        email = st.text_input("Email", placeholder="Email")
        password = st.text_input(
            "Senha", type="password", placeholder="Senha"
        )


        
        if st.button("Login"):
            user_instance = User(email=email, password=password)
            user = user_instance.authenticate_user()

            if user:
                logged_user["id"] = user["id"]
                logged_user["name"] = user["name"]
                logged_user["email"] = user["email"]
                st.success(f"Bem vindo, {user['name']}!")
                st.experimental_set_query_params(page="Profile")
            else:
                st.error("Email ou senha inválidas. Tente novamente.")
            st.rerun()
    else:
        st.write("")

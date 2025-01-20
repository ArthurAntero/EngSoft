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

        col1, col2, col3 = st.columns([1, 1, 1])

        with col1:
            if st.button("Login"):
                user_instance = User(email=email, password=password)
                user = user_instance.authenticate_user()

                if user:
                    logged_user["id"] = user["id"]
                    logged_user["name"] = user["name"]
                    logged_user["email"] = user["email"]

                    st.success(f"Bem vindo, {user['name']}!")
                    st.experimental_set_query_params(page="profile")
                    st.rerun()
                else:
                    st.error("Email ou senha inválidas. Tente novamente.")

        with col2:
            if st.button("Criar conta"):
                st.experimental_set_query_params(page="signup")

        with col3:
            if st.button("Esqueci a senha"):
                st.experimental_set_query_params(page="forgot_password")
    else:
        st.write(f"Bem vindo de volta, {logged_user['name']}!")

        if st.button("Logout"):
            logged_user["id"] = None
            logged_user["name"] = None
            logged_user["email"] = None

            st.experimental_set_query_params(page="login")  # Volta à página de login
            st.rerun()

        if st.button("Minha conta"):
            st.experimental_set_query_params(page="profile")

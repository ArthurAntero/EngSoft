import time
import streamlit as st
from api.users import User


def signup_page():
    st.header("Criar uma nova conta")

    email = st.text_input("Email", placeholder="Email")
    name = st.text_input("Nome", placeholder="Nome")
    password = st.text_input(
        "Senha", type="password", placeholder="Senha"
    )
    confirm_password = st.text_input(
        "Confirmar Senha", type="password", placeholder="Confirme sua senha"
    )

    if st.button("Cadastrar"):
        if not email or not name or not password or not confirm_password:
            st.error("Por favor, preencha todos os campos.")
        elif password != confirm_password:
            st.error("As senhas não coincidem.")
        else:
            user_instance = User(email=email, name=name, password=password)
            if user_instance.create_user():
                st.success("Conta criada com sucesso.")
                time.sleep(2)
                st.experimental_set_query_params(page="Login")
                st.rerun()
            else:
                st.error("Erro ao criar a conta. Por favor, tente novamente.")

        st.rerun()

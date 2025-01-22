import streamlit as st
import time
from api.users import User


def forgot_password_page():
    st.header("Esqueci a senha")

    email = st.text_input("Email", placeholder="Email")
    new_password = st.text_input(
        "Nova Senha", type="password", placeholder="Nova Senha"
    )
    confirm_new_password = st.text_input(
        "Confirme Nova Senha", type="password", placeholder="Confirme Nova Senha"
    )

    if st.button("Redefinir senha"):
        if not email or not new_password or not confirm_new_password:
            st.error("Por favor, preencha todos os campos.")
        elif new_password != confirm_new_password:
            st.error("As senhas não são iguais.")
        else:
            user_instance = User(email=email)
            if user_instance.reset_password(new_password=new_password):
                st.success("Senha redefinida com sucesso!")
                time.sleep(2)
                st.experimental_set_query_params(page="Login")
                st.rerun()
            else:
                st.error("Erro redefinindo senha. Por favor, tente novamente.")

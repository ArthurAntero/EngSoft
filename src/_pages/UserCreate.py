import streamlit as st
from api.users import User


def signup_page():
    st.header("Criar nova conta")

    email = st.text_input("Email", placeholder="Email")
    name = st.text_input("Nome", placeholder="Nome")
    password = st.text_input(
        "Senha", type="password", placeholder="Senha"
    )
    confirm_password = st.text_input(
        "Confirmar Senha", type="password", placeholder="Confirme a senha"
    )

    if st.button("Criar"):
        if not email or not name or not password or not confirm_password:
            st.error("Preecha todas os campos.")
        elif password != confirm_password:
            st.error("Coloque a mesma senha nos campos.")
        else:
            user_instance = User(email=email, name=name, password=password)
            if user_instance.create_user():
                st.success("Conta criada com sucesso.")
            else:
                st.error("Erro ao criar conta. Tente novamente.")

        st.rerun()


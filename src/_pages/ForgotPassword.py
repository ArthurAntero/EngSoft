import streamlit as st
from api.users import User


def forgot_password_page():
    st.header("Esqueceu a senha")

    email = st.text_input("Email", placeholder="Email")
    new_password = st.text_input(
        "NNova senha", type="password", placeholder="Nova senha"
    )
    confirm_new_password = st.text_input(
        "Confirmar nova senha", type="password", placeholder="Confirme nova senha"
    )

    if st.button("Resetar senha"):
        if not email or not new_password or not confirm_new_password:
            st.error("Preencha todos os campos.")
        elif new_password != confirm_new_password:
            st.error("Coloque a mesma senha nos campos.")
        else:
            user_instance = User(email=email)
            if user_instance.reset_password(new_password=new_password):
                st.success("Senha resetada com sucesso!")
            else:
                st.error("Erro ao resetar senha. Tente novamente.")
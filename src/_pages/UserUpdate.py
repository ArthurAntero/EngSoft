import time
import streamlit as st
from api.users import User
from globals import logged_user

def update_user_page():
    if not logged_user or not logged_user.get("id"):
        st.error("Você precisa estar logado para atualizar seu perfil.")
        return

    st.title("Atualizar Perfil de Usuário")

    # Exibir os dados atuais do usuário
    user_model = User()
    user_model.id = logged_user["id"]
    current_email = logged_user["email"]
    current_name = logged_user["name"]

    with st.form(key="update_user_form"):
        new_email = st.text_input("Email", value=current_email)
        new_name = st.text_input("Nome", value=current_name)

        submit_button = st.form_submit_button("Atualizar Perfil")

        if submit_button:
            if not new_email or not new_name:
                st.error("Os campos de email e nome devem ser preenchidos.")
                return

            user_model.email = new_email
            user_model.name = new_name

            if user_model.update_user():
                st.success("Perfil atualizado com sucesso!")
                time.sleep(1)
                logged_user["email"] = new_email
                logged_user["name"] = new_name
                st.experimental_set_query_params(page="Profile")
                st.rerun()
            else:
                st.error("Falha ao atualizar o perfil. Por favor, tente novamente.")

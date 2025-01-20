import streamlit as st
from api.users import User
from globals import logged_user


def edit_profile_page():
    if logged_user.get("id") is not None:
        st.header("Edite sua conta")

        new_email = st.text_input("Email", value=logged_user["email"])
        new_name = st.text_input("Nome", value=logged_user["name"])

        if st.button("Save Changes"):
            user_instance = User(
                id=logged_user["id"], email=new_email, name=new_name
            )
            if user_instance.update_user():
                logged_user["email"] = new_email
                logged_user["name"] = new_name
                st.success("Você atualizou a sua conta")
            else:
                st.error("Erro ao atualizar conta. Tente novamente.")

        if st.button("Minha conta"):
            st.experimental_set_query_params(page="profile")
            st.rerun()
    else:
        st.warning("Você precisa estar logado para acessar esta página.")
        st.experimental_set_query_params(page="login")
        st.rerun()

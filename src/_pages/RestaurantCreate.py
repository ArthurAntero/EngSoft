import time
import streamlit as st
from api.restaurants import Restaurant
from globals import logged_user

def create_restaurant_page():
    if logged_user.get("id") is not None:
        st.header("Criar um Novo Restaurante")

        name = st.text_input("Nome do Restaurante")
        location = st.text_input("Localização")
        description = st.text_area("Descrição")
        category = st.text_input("Categoria")

        if st.button("Criar Restaurante"):
            restaurant_instance = Restaurant(
                name=name, 
                location=location, 
                description=description, 
                category=category, 
                user_id=logged_user["id"]
            )
            
            if restaurant_instance.create_restaurant(logged_user["id"]):
                st.success("Restaurante criado com sucesso!")
                time.sleep(2)
                st.experimental_set_query_params(page="Restaurants")
                st.rerun()
            else:
                st.error("Ocorreu um erro ao criar o restaurante. Por favor, tente novamente.")
            st.rerun()
    else:
        st.warning("Você precisa fazer login para criar um restaurante.")
        st.experimental_set_query_params(page="login")
        st.rerun()

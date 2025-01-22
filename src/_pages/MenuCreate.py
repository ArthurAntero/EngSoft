import time
import streamlit as st
from api.menus import Menu
from api.restaurants import Restaurant
from globals import logged_user

def create_menu_page():
    if logged_user.get("id") is not None:
        st.header("Criar um Novo Menu")

        restaurant_model = Restaurant()
        user_restaurants = restaurant_model.fetch_restaurants_by_user(logged_user["id"])

        if not user_restaurants:
            st.info("Você precisa criar um restaurante antes de adicionar um menu.")
            return

        restaurant_options = {restaurant["name"]: restaurant["id"] for restaurant in user_restaurants}
        selected_restaurant = st.selectbox("Selecione um Restaurante", list(restaurant_options.keys()))

        name = st.text_input("Nome do Menu")
        description = st.text_area("Descrição")
        menu_photo = st.file_uploader("Carregar uma Foto do Menu", type=["jpg", "jpeg", "png"])

        if st.button("Criar Menu"):
            if selected_restaurant and name and description:
                photo_bytes = None
                if menu_photo:
                    photo_bytes = menu_photo.read()

                menu_instance = Menu(
                    name=name,
                    description=description,
                    menu_photo=photo_bytes,
                    restaurant_id=restaurant_options[selected_restaurant],
                    user_id=logged_user["id"],
                )

                if menu_instance.create_menu():
                    st.success("Menu criado com sucesso!")
                    time.sleep(2)
                    st.experimental_set_query_params(page="Menus")
                    st.rerun()
                else:
                    st.error("Ocorreu um erro ao criar o cardápio. Por favor, tente novamente.")
            else:
                st.error("Por favor, preencha todos os campos obrigatórios.")
    else:
        st.warning("Você precisa fazer login para criar um menu.")
        st.experimental_set_query_params(page="login")
        st.rerun()

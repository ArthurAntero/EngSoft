import time
import streamlit as st
from api.restaurants import Restaurant
from globals import logged_user


def update_restaurant_page():
    if not logged_user or not logged_user.get("id"):
        st.error("Você precisa estar logado para atualizar um restaurante.")
        return

    st.title("Atualizar um Restaurante")

    restaurant_model = Restaurant()
    user_restaurants = restaurant_model.fetch_restaurants_by_user(logged_user["id"])

    if not user_restaurants:
        st.info("Você não tem restaurantes para atualizar.")
        return

    restaurant_names = [restaurant["name"] for restaurant in user_restaurants]
    selected_restaurant_name = st.selectbox(
        "Selecione um restaurante para atualizar", options=["Selecione um restaurante"] + restaurant_names
    )

    selected_restaurant = None
    if selected_restaurant_name != "Selecione um restaurante":
        selected_restaurant = next(
            (restaurant for restaurant in user_restaurants if restaurant["name"] == selected_restaurant_name), None
        )

    if selected_restaurant:
        with st.form(key="update_restaurant_form"):
            name = st.text_input("Nome do Restaurante", value=selected_restaurant["name"])
            location = st.text_input("Localização", value=selected_restaurant["location"])
            description = st.text_area("Descrição", value=selected_restaurant["description"])
            category = st.text_input("Categoria", value=selected_restaurant["category"])

            submit_button = st.form_submit_button("Atualizar Restaurante")

            if submit_button:
                if not name or not location or not description or not category:
                    st.error("Todos os campos devem ser preenchidos.")
                    return

                restaurant_model.id = selected_restaurant["id"]
                restaurant_model.name = name
                restaurant_model.location = location
                restaurant_model.description = description
                restaurant_model.category = category

                if restaurant_model.update_restaurant():
                    st.success("Restaurante atualizado com sucesso!")
                    time.sleep(2)
                    st.experimental_set_query_params(page="Restaurants")
                    st.rerun()
                else:
                    st.error("Falha ao atualizar o restaurante.")
    else:
        st.info("Por favor, selecione um restaurante para editar.")

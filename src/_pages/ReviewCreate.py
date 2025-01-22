import time
import streamlit as st
from api.reviews import Review
from api.restaurants import Restaurant
from globals import logged_user

def create_review_page():
    if not logged_user or not logged_user.get("id"):
        st.error("Você precisa estar logado para criar uma avaliação.")
        return

    st.title("Criar uma Avaliação")

    restaurant_model = Restaurant()
    review_model = Review()

    restaurants = restaurant_model.fetch_all_restaurants()

    if not restaurants:
        st.info("Nenhum restaurante disponível. Por favor, crie um restaurante para adicionar uma avaliação.")
        return

    restaurant_names = [restaurant["name"] for restaurant in restaurants]

    with st.form(key="create_review_form"):
        description = st.text_area("Descrição da Avaliação", max_chars=500)
        grade = st.slider("Nota", min_value=0.0, max_value=5.0, step=0.1)
        restaurant_name = st.selectbox("Selecione um Restaurante", options=restaurant_names)

        submit_button = st.form_submit_button("Enviar Avaliação")

    if submit_button:
        if not description or not restaurant_name:
            st.error("Todos os campos devem ser preenchidos.")
            return

        restaurant_id = restaurant_model.fetch_restaurant_id_by_name(restaurant_name)

        if not restaurant_id:
            st.error("Erro ao encontrar o restaurante selecionado.")
            return

        review_model.description = description
        review_model.grade = grade
        review_model.restaurant_id = restaurant_id
        review_model.user_id = logged_user["id"]

        if review_model.create_review(logged_user["id"]):
            st.success("Avaliação criada com sucesso!")
            time.sleep(1)
            st.experimental_set_query_params(page="Reviews")
            st.rerun()
        else:
            st.error("Falha ao criar a avaliação.")

import streamlit as st
from api.reviews import Review
from api.restaurants import Restaurant
from globals import logged_user

def create_review_page():
    # Verifica se o usuário está logado
    if not logged_user or not logged_user.get("id"):
        st.error("You must be logged in to create a review.")
        return

    st.title("Create a Review")

    restaurant_model = Restaurant()
    review_model = Review()

    # Busca todos os restaurantes para o dropdown
    restaurants = restaurant_model.fetch_all_restaurants()
    restaurant_names = [restaurant["name"] for restaurant in restaurants]

    with st.form(key="create_review_form"):
        # Campos do formulário
        description = st.text_area("Review Description", max_chars=500)
        grade = st.slider("Grade", min_value=0.0, max_value=5.0, step=0.1)
        restaurant_name = st.selectbox("Select a Restaurant", options=restaurant_names)

        # Botão de submissão
        submit_button = st.form_submit_button("Submit Review")

    if submit_button:
        if not description or not restaurant_name:
            st.error("All fields must be filled.")
            return

        # Busca o ID do restaurante selecionado
        restaurant_id = restaurant_model.fetch_restaurant_id_by_name(restaurant_name)

        if not restaurant_id:
            st.error("Error finding the selected restaurant.")
            return

        # Preenche os dados do review
        review_model.description = description
        review_model.grade = grade
        review_model.restaurant_id = restaurant_id
        review_model.user_id = logged_user["id"]

        # Cria o review
        if review_model.create_review(logged_user["id"]):
            st.success("Review created successfully!")
        else:
            st.error("Failed to create review.")

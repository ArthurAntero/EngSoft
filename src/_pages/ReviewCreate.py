import streamlit as st
from api.reviews import Review
from api.restaurants import Restaurant
from globals import logged_user

def create_review_page():
    query_params = st.experimental_get_query_params()
    restaurant_name = query_params.get("restaurant", [""])[0]

    restaurant_model = Restaurant()
    review_model = Review()

    restaurant_id = restaurant_model.fetch_restaurant_id_by_name(restaurant_name)

    if not restaurant_id:
        st.error("Restaurant not found.")
        return

    with st.form(key="create_review_form"):
        description = st.text_area("Review Description", max_chars=500)
        grade = st.slider("Grade", min_value=0.0, max_value=5.0, step=0.1)
        submit_button = st.form_submit_button("Submit Review")

    if submit_button:
        if not logged_user["id"]:
            st.error("You must be logged in to create a review.")
            return

        review_model.description = description
        review_model.grade = grade
        review_model.restaurant_id = restaurant_id
        review_model.user_id = logged_user["id"]

        if review_model.create_review(logged_user["id"]):
            st.success("Review created successfully!")
            st.experimental_set_query_params(page="List Reviews", restaurant=restaurant_name)
        else:
            st.error("Failed to create review.")

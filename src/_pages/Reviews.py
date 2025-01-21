import streamlit as st
from api.reviews import Review
from globals import logged_user

def list_reviews_page():
    query_params = st.experimental_get_query_params()
    restaurant_name = query_params.get("restaurant", [""])[0]

    review_model = Review()

    reviews = review_model.fetch_reviews_by_restaurant_name(restaurant_name)

    if not reviews:
        st.info("No reviews found.")
    else:
        for review in reviews:
            description = review.get("description")
            grade = review.get("grade")
            st.write(f"**Grade:** {grade:.2f}")
            st.write(f"**Review:** {description}")
            st.markdown("---")

    st.markdown("---")
    if logged_user and logged_user.get("id"):
        if st.button("Create Review"):
            st.experimental_set_query_params(page="Create Review", restaurant=restaurant_name)
    else:
        st.info("You must be logged in to create a review.")

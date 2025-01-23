import streamlit as st
from api.reviews import Review
from api.restaurants import Restaurant
from globals import logged_user

def update_review_page():
    if not logged_user or not logged_user.get("id"):
        st.error("You must be logged in to update a review.")
        return

    st.title("Update a Review")

    review_model = Review()
    user_reviews = [
        review for review in review_model.fetch_all_reviews()
        if review["user_id"] == logged_user["id"]
    ]

    if not user_reviews:
        st.info("You have no reviews to update.")
        return

    review_options = ["Select a review"] + [
        f"{review['restaurant_name']} - {review['description'][:30]}..."
        for review in user_reviews
    ]
    selected_review_index = st.selectbox(
        "Select a review to update", options=list(range(len(review_options))), 
        format_func=lambda x: review_options[x]
    )

    selected_review = (
        user_reviews[selected_review_index - 1] if selected_review_index > 0 else None
    )

    if selected_review:
        with st.form(key="update_review_form"):
            description = st.text_area("Review Description", value=selected_review["description"], max_chars=500)
            grade = st.slider("Grade", min_value=0.0, max_value=5.0, step=0.1, value=selected_review["grade"])

            submit_button = st.form_submit_button("Update Review")

            if submit_button:
                if not description:
                    st.error("Description must be filled.")
                    return

                review_model.id = selected_review["id"]
                review_model.description = description
                review_model.grade = grade

                if review_model.update_review():
                    st.success("Review updated successfully!")
                    st.experimental_set_query_params(page="Reviews")
                    st.rerun()
                else:
                    st.error("Failed to update the review.")
    else:
        st.info("Please select a review to edit.")

import streamlit as st
from api.reviews import Review
from globals import logged_user

def list_reviews_page():
    review_model = Review()
    reviews = review_model.fetch_all_reviews()

    st.title("All Reviews")

    if not reviews:
        st.info("No reviews found.")
    else:
        for review in reviews:
            review_id = review.get("id")
            description = review.get("description")
            grade = review.get("grade")
            user_name = review.get("user_name")
            restaurant_name = review.get("restaurant_name")
            user_id = review.get("user_id")

            with st.container():
                st.subheader(f"Restaurant: {restaurant_name}")
                st.write(f"**User:** {user_name}")
                st.write(f"**Description:** {description}")
                st.write(f"**Stars:** {grade:.1f}")

                if user_id == logged_user["id"]:
                    if st.button("Delete Review", key=f"delete_{review_id}", help="Delete this review"):
                        if review_model.delete_review(review_id):
                            st.success("Review deleted successfully!")
                            st.rerun()
                        else:
                            st.error("Failed to delete the review.")
                st.markdown("---")

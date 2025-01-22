import streamlit as st
from api.restaurants import Restaurant
from globals import logged_user


def update_restaurant_page():
    if not logged_user or not logged_user.get("id"):
        st.error("You must be logged in to update a restaurant.")
        return

    st.title("Update a Restaurant")

    restaurant_model = Restaurant()
    user_restaurants = restaurant_model.fetch_restaurants_by_user(logged_user["id"])

    if not user_restaurants:
        st.info("You have no restaurants to update.")
        return

    restaurant_names = [restaurant["name"] for restaurant in user_restaurants]
    selected_restaurant_name = st.selectbox(
        "Select a restaurant to update", options=["Select a restaurant"] + restaurant_names
    )

    selected_restaurant = None
    if selected_restaurant_name != "Select a restaurant":
        selected_restaurant = next(
            (restaurant for restaurant in user_restaurants if restaurant["name"] == selected_restaurant_name), None
        )

    if selected_restaurant:
        with st.form(key="update_restaurant_form"):
            name = st.text_input("Restaurant Name", value=selected_restaurant["name"])
            location = st.text_input("Location", value=selected_restaurant["location"])
            description = st.text_area("Description", value=selected_restaurant["description"])
            category = st.text_input("Category", value=selected_restaurant["category"])

            submit_button = st.form_submit_button("Update Restaurant")

            if submit_button:
                if not name or not location or not description or not category:
                    st.error("All fields must be filled.")
                    return

                restaurant_model.id = selected_restaurant["id"]
                restaurant_model.name = name
                restaurant_model.location = location
                restaurant_model.description = description
                restaurant_model.category = category

                if restaurant_model.update_restaurant():
                    st.success("Restaurant updated successfully!")
                    st.experimental_set_query_params(page="Restaurants")
                    st.rerun()
                else:
                    st.error("Failed to update the restaurant.")
    else:
        st.info("Please select a restaurant to edit.")

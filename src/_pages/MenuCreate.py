import streamlit as st
from api.menus import Menu
from api.restaurants import Restaurant
from globals import logged_user

def create_menu_page():
    if logged_user.get("id") is not None:
        st.header("Create a New Menu")

        restaurant_model = Restaurant()
        user_restaurants = restaurant_model.fetch_restaurants_by_user(logged_user["id"])

        if not user_restaurants:
            st.warning("You need to create a restaurant before adding a menu.")
            st.experimental_set_query_params(page="Create Restaurant")
            st.experimental_rerun()

        restaurant_options = {restaurant["name"]: restaurant["id"] for restaurant in user_restaurants}
        selected_restaurant = st.selectbox("Select a Restaurant", list(restaurant_options.keys()))

        name = st.text_input("Menu Name")
        description = st.text_area("Description")
        menu_photo = st.file_uploader("Upload a Menu Photo", type=["jpg", "jpeg", "png"])

        if st.button("Create Menu"):
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
                    st.success("Menu created successfully!")
                    st.experimental_set_query_params(page="Menus")
                    st.experimental_rerun()
                else:
                    st.error("There was an error creating the menu. Please try again.")
            else:
                st.error("Please fill in all required fields.")
    else:
        st.warning("You need to log in to create a menu.")
        st.experimental_set_query_params(page="login")
        st.experimental_rerun()

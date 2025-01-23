import time
import streamlit as st
from api.menus import Menu
from api.restaurants import Restaurant
from globals import logged_user

def update_menu_page():
    if not logged_user or not logged_user.get("id"):
        st.error("You need to be logged in to update a menu.")
        return

    st.title("Update a Menu")

    menu_model = Menu()
    restaurant_model = Restaurant()

    # Fetch the logged user's restaurants
    user_restaurants = restaurant_model.fetch_restaurants_by_user(logged_user["id"])
    if not user_restaurants:
        st.info("You don't have any restaurants to update menus.")
        return

    restaurant_options = {restaurant["name"]: restaurant["id"] for restaurant in user_restaurants}
    selected_restaurant = st.selectbox("Select a Restaurant", list(restaurant_options.keys()))

    if selected_restaurant:
        # Fetch menus for the selected restaurant
        restaurant_id = restaurant_options[selected_restaurant]
        menus = [
            menu for menu in menu_model.fetch_all_menus() 
            if menu["restaurant_id"] == restaurant_id and menu["user_id"] == logged_user["id"]
        ]

        if not menus:
            st.info(f"There are no menus to update in the restaurant '{selected_restaurant}'.")
            return

        menu_options = {menu["name"]: menu for menu in menus}
        selected_menu_name = st.selectbox("Select a Menu", list(menu_options.keys()))

        selected_menu = menu_options[selected_menu_name]

        if selected_menu:
            with st.form(key="update_menu_form"):
                name = st.text_input("Menu Name", value=selected_menu["name"])
                description = st.text_area("Description", value=selected_menu["description"])
                menu_photo = st.file_uploader("Update Menu Photo", type=["jpg", "jpeg", "png"])

                submit_button = st.form_submit_button("Update Menu")

                if submit_button:
                    if not name or not description:
                        st.error("All fields must be filled.")
                        return

                    photo_bytes = None
                    if menu_photo:
                        photo_bytes = menu_photo.read()

                    menu_instance = Menu(
                        id=selected_menu["id"],
                        name=name,
                        description=description,
                        menu_photo=photo_bytes,
                        restaurant_id=restaurant_id,
                        user_id=logged_user["id"],
                    )

                    if menu_instance.update_menu():
                        st.success("Menu successfully updated!")
                        st.experimental_set_query_params(page="Menus")
                        st.rerun()
                    else:
                        st.error("Failed to update the menu.")

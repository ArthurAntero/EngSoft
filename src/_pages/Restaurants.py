import streamlit as st
from api.restaurants import Restaurant
from globals import logged_user

def list_restaurants_page():
    st.header("Restaurants")
    st.markdown("---")

    restaurant_model = Restaurant()
    restaurants = restaurant_model.fetch_all_restaurants()

    if not restaurants:
        st.info("No restaurants found.")
        return

    for restaurant in restaurants:
        restaurant_id = restaurant.get("id")
        name = restaurant.get("name")
        category = restaurant.get("category")
        description = restaurant.get("description")
        location = restaurant.get("location")
        total_grade = restaurant.get("total_grade")

        with st.container():
            st.subheader(name)
            st.write(f"**Category:** {category}")
            st.write(f"**Description:** {description}")
            st.write(f"**Location:** {location}")
            st.write(f"**Stars:** {total_grade:.1f}")

            if restaurant.get("user_id") == logged_user["id"]:
                if st.button(f"Delete {name}", key=f"delete_{restaurant_id}"):
                    if restaurant_model.delete_restaurant(restaurant_id):
                        st.success(f"Restaurant '{name}' deleted successfully.")
                        st.rerun()
                    else:
                        st.error(f"Failed to delete restaurant '{name}'.")
        st.markdown("---")


import streamlit as st
from api.restaurants import Restaurant

def list_restaurants_page():
    st.header("Restaurants")

    restaurant_model = Restaurant()

    restaurants = restaurant_model.fetch_all_restaurants()

    if not restaurants:
        st.info("No restaurants found.")
        return

    for restaurant in restaurants:
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
            

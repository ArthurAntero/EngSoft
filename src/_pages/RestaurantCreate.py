import streamlit as st
from api.restaurants import Restaurant
from globals import logged_user

def create_restaurant_page():
    if logged_user.get("id") is not None:
        st.header("Create a New Restaurant")

        name = st.text_input("Restaurant Name")
        location = st.text_input("Location")
        description = st.text_area("Description")
        category = st.text_input("Category")

        if st.button("Create Restaurant"):
            restaurant_instance = Restaurant(
                name=name, 
                location=location, 
                description=description, 
                category=category, 
                
                user_id=logged_user["id"]
            )
            
            if restaurant_instance.create_restaurant(logged_user["id"]):
                st.success("Restaurant created successfully!")
                st.experimental_set_query_params(page="Restaurants")
                st.experimental_rerun()
            else:
                st.error("There was an error creating the restaurant. Please try again.")
            st.rerun()
    else:
        st.warning("You need to log in to create a restaurant.")
        st.experimental_set_query_params(page="login")
        st.experimental_rerun()

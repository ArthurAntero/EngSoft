import sys
import os
import streamlit as st
from streamlit_option_menu import option_menu
from globals import logged_user

from _pages.Login import login_page
from _pages.UserCreate import signup_page
from _pages.ForgotPassword import forgot_password_page
from _pages.Profile import profile_page
from _pages.UserUpdate import edit_profile_page
from _pages.ListRestaurants import list_restaurants_page
from _pages.ListMenus import list_menus_page
from _pages.ListReviews import list_reviews_page
from _pages.AddRestaurants import add_restaurants_page
from _pages.AddMenus import add_menus_page
from _pages.AddReviews import add_reviews_page
from _pages.EditRestaurants import edit_restaurants_page
from _pages.EditMenus import edit_menus_page
from _pages.EditReviews import edit_reviews_page


user_menu = [
    "Profile",
    "Add Restaurants",
    "Edit Restaurants",
    "List Restaurants",
    "Add Menus",
    "Edit Menus",
    "List Menus",
    "Add Review",
    "Edit Reviews",
    "List Reviews",
]

user_icons = [
    "house",
    "plus-circle",
    "pencil",
    "list-ul",
    "plus-circle",
    "pencil",
    "list-ul",
    "plus-circle",
    "pencil",
    "list-ul",
]

no_logged_menu = [
    "Login",
    "List Restaurants",
    "List Menus",
    "List Reviews",
]

no_logged_icons = [
    "door-open",
    "list-ul",
    "list-ul",
    "list-ul",
]

# Funções para definir menus baseados no estado do usuário
def choose_menu():
    if logged_user["id"] is None:
        return no_logged_menu
    else:
        return user_menu


def choose_icons():
    if logged_user["id"] is None:
        return no_logged_icons
    else:
        return user_icons

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

query_params = st.experimental_get_query_params()
page = query_params.get("page", ["login"])[0]

# Sidebar com menu
with st.sidebar:
    st.write("# BiteCritic")

    selected = option_menu(
        menu_title=None,
        options=choose_menu(),
        icons=choose_icons(),
        menu_icon="cast",
        default_index=choose_menu().index(page) if page in choose_menu() else 0,
        styles={
            "nav-link": {
                "font-size": "1.25rem",
                "text-align": "left",
                "margin": "0.375rem 0",
            },
        },
    )
    
    st.experimental_set_query_params(page=selected)

if page == "Login":
    login_page()
elif page == "signup":
    signup_page()
elif page == "forgot_password":
    forgot_password_page()
elif page == "Profile":
    profile_page()
elif page == "edit_profile":
    edit_profile_page()
elif page == "List Restaurants":
    list_restaurants_page()
elif page == "List Menus":
    list_menus_page()
elif page == "List Reviews":
    list_reviews_page()
elif page == "Add Restaurants":
    add_restaurants_page()
elif page == "Add Menus":
    add_menus_page()
elif page == "Add Review":
    add_reviews_page()
elif page == "Edit Restaurants":
    edit_restaurants_page()
elif page == "Edit Menus":
    edit_menus_page()
elif page == "Edit Reviews":
    edit_reviews_page()
else:
    st.error("Page not found.")
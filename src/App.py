import sys
import os
import streamlit as st
from streamlit_option_menu import option_menu
from globals import logged_user

from _pages.Login import login_page
from _pages.UserCreate import signup_page
from _pages.ForgotPassword import forgot_password_page
from _pages.Profile import profile_page
from _pages.Restaurants import list_restaurants_page
from _pages.Menus import list_menus_page
from _pages.Reviews import list_reviews_page
from _pages.RestaurantCreate import create_restaurant_page
from _pages.MenuCreate import create_menu_page
from _pages.ReviewCreate import create_review_page
from _pages.RestaurantUpdate import update_restaurant_page
from _pages.ReviewUpdate import update_review_page
from _pages.UserUpdate import update_user_page


user_menu = [
    "Perfil",
    "Editar Perfil",
    "Restaurantes",
    "Criar Restaurante",
    "Editar Restaurante",
    "Avaliações",
    "Criar Avaliação",
    "Editar Avaliação",
    "Menus",
    "Criar Menu"
]

user_icons = [
    "house",
    "pencil",
    "list-ul",
    "plus-circle",
    "pencil",
    "list-ul",
    "plus-circle",
    "pencil",
    "list-ul",
    "plus-circle",
]

no_logged_menu = [
    "Login",
    "Criar conta",
    "Esqueci a senha",
]

no_logged_icons = [
    "door-open",
    "plus-circle",
    "pencil",
]

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
page = query_params.get("page", ["Login"])[0]

with st.sidebar:
    st.write("# BiteCritique")

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
    
    # Atualizar o parâmetro de página na URL e recarregar
    if selected != page:
        st.experimental_set_query_params(page=selected)
        st.experimental_rerun()

if page == "Login":
    login_page()
elif page == "Criar conta":
    signup_page()
elif page == "Editar Perfil":
    update_user_page()
elif page == "Esqueci a senha":
    forgot_password_page()
elif page == "Perfil":
    profile_page()
elif page == "Restaurantes":
    list_restaurants_page()
elif page == "Menus":
    list_menus_page()
elif page == "Avaliações":
    list_reviews_page()
elif page == "Criar Restaurante":
    create_restaurant_page()
elif page == "Criar Menu":
    create_menu_page()
elif page == "Criar Avaliação":
    create_review_page()
elif page == "Editar Restaurante":
    update_restaurant_page()
elif page == "Editar Avaliação":
    update_review_page()
else:
    st.error("Page not found.")
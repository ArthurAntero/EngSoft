import sys
import os

import streamlit as st
from streamlit_option_menu import option_menu
from globals import logged_user

from _pages import (
    Login,
    Add_Restaurants,
    Add_Menus,
    Add_Reviews,
    Edit_Restaurants,
    Edit_Menus,
    Edit_Reviews,
    List_Restaurants,
    List_Menus,
    List_Reviews,
)

# Adiciona o diretório "src" ao Python Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

with open('src/globals.py', 'r') as file:
    exec(file.read())
    
user_menu=[
    "Add Restaurants", 
    "Edit Restaurants",
    "List Restaurants",

    "Add Menus",
    "Edit Menus",
    "List Menus",

    "Add Review", 
    "Edit Menus",
    "List Review",
]

user_icons=[
    "house",

    "plus-circle",
    "pencil",
    "list-ul",

    "plus-circle",
    "pencil",
    "list-ul",

    "plus-circle",
    "list-ul",

    "plus-circle",
    "pencil",
    "list-ul",
]


no_logged_menu=[
    "Login",
    "List Restaurants",
    "List Menus",
    "List Reviews",
]

no_logged_icons=[
    "dor-open",
    "list-ul",
    "list-ul",
    "list-ul",
]

def choose_menu():
    if logged_user['id'] is None:
        return no_logged_menu
    else:
        return user_menu
    
def choose_icons():
    if logged_user['id'] is None:
        return no_logged_icons
    else:
        return user_icons

with st.sidebar:
    st.write(f'# BiteCritic')

    selected = option_menu(
        menu_title=None,
        options=choose_menu(),
        icons=choose_icons(),
        menu_icon="cast",
        default_index=0,
        styles={
            "nav-link": {
                "font-size": "1.25rem", 
                "text-align": "left", 
                "margin":"0.375rem 0", 
            },
        }
    )

if selected=="Login":
    Login.create_page()

if selected=="Add Restaurants":
    Add_Restaurants.create_page()

if selected=="Add Menus":
    Add_Menus.create_page()

if selected=="Add Reviews":
    Add_Reviews.create_page()

if selected=="Edit Restaurants":
    Edit_Restaurants.create_page()

if selected=="Edit Menus":
    Edit_Menus.create_page()

if selected=="Edit Reviews":
    Edit_Reviews.create_page()

if selected=="List Restaurants":
    List_Restaurants.create_page()

if selected=="List Menus":
    List_Menus.create_page()

if selected=="List Reviews":
    List_Reviews.create_page()


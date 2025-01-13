import streamlit as st
from streamlit_option_menu import option_menu
from globals import logged_user
from _pages import (
    Add_Books, 
    Add_Loan, 
    Add_Teaching_Materials, 
    Add_Users, 
    Edit_Books, 
    Edit_Teaching_Materials, 
    Edit_Users, 
    List_Books, 
    List_Loans, 
    List_Teaching_Materials, 
    List_Users,
    Login,
    Home
)

with open('src/globals.py', 'r') as file:
    exec(file.read())

admin_menu=[
    "Home",

    "Add Books", 
    "Edit Books",
    "List Books",

    "Add Teaching Materials",
    "Edit Teaching Materials",
    "List Teaching Materials",

    "Add Loan", 
    "List Loans",

    "Add Users", 
    "Edit Users",
    "List Users"
]

admin_icons=[
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

member_menu=[
    "Home",
    "Add Loan", 
    "List Books",
    "List Loans",
    "List Teaching Materials",
]

member_icons=[
    "house",
    "plus-circle",
    "list-ul",
    "list-ul",
    "list-ul",
]

no_logged_menu=[
    "Login",
    "List Books",
    "List Teaching Materials",
]

no_logged_icons=[
    "dor-open",
    "list-ul",
    "list-ul",
]

def choose_menu():
    if logged_user['role'] is None:
        return no_logged_menu
    elif logged_user["role"] == 'ADMIN':
        return admin_menu
    elif logged_user["role"] == 'MEMBER':
        return member_menu
    

def choose_icons():
    if logged_user['role'] is None:
        return no_logged_icons
    elif logged_user["role"] == 'ADMIN':
        return admin_icons
    elif logged_user["role"] == 'MEMBER':
        return member_icons
    

with st.sidebar:
    st.write(f'# LabLibrary')

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

if selected=="Home":
    Home.create_page()

if selected=="Add Books":
    Add_Books.create_page()

if selected=="Add Loan":
    Add_Loan.create_page()

if selected=="Add Teaching Materials":
    Add_Teaching_Materials.create_page()

if selected=="Add Users":
    Add_Users.create_page()

if selected=="Edit Books":
    Edit_Books.create_page()

if selected=="Edit Teaching Materials":
    Edit_Teaching_Materials.create_page()

if selected=="Edit Users":
    Edit_Users.create_page()

if selected=="List Teaching Materials":
    List_Teaching_Materials.create_page()

if selected=="List Loans":
    List_Loans.create_page()

if selected=="List Users":
    List_Users.create_page()

if selected=="List Books":
    List_Books.create_page()

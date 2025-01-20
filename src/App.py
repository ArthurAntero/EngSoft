import sys
import os
import streamlit as st
from _pages.Login import login_page
from _pages.UserCreate import signup_page
from _pages.ForgotPassword import forgot_password_page
from _pages.Profile import profile_page
from _pages.UserUpdate import edit_profile_page

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

query_params = st.experimental_get_query_params()
page = query_params.get("page", ["login"])[0]

if page == "login":
    login_page()
elif page == "signup":
    signup_page()
elif page == "forgot_password":
    forgot_password_page()
elif page == "profile":
    profile_page()
elif page == "edit_profile":
    edit_profile_page()
else:
    st.error("Page not found.")
import streamlit as st
from api.users import User


def forgot_password_page():
    st.header("Forgot Password")

    email = st.text_input("Email", placeholder="Email")
    new_password = st.text_input(
        "New Password", type="password", placeholder="New Password"
    )
    confirm_new_password = st.text_input(
        "Confirm New Password", type="password", placeholder="Confirm New Password"
    )

    if st.button("Reset Password"):
        if not email or not new_password or not confirm_new_password:
            st.error("Please fill in all fields.")
        elif new_password != confirm_new_password:
            st.error("Passwords do not match.")
        else:
            user_instance = User(email=email)
            if user_instance.reset_password(new_password=new_password):
                st.success("Password reset successfully!")
            else:
                st.error("Error resetting password. Please try again.")

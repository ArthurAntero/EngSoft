import streamlit as st
from api.users import User

def create_page():
  ROLES = ['MEMBER', 'ADMIN']

  st.header('Add a New User')

  username = st.text_input('Username')
  first_name = st.text_input('First name')
  last_name = st.text_input('Last name')
  user_photo_url = st.text_input('User photo url')
  role = st.selectbox('Role', ROLES)
  password = st.text_input('Password', type='password')

  if st.button('Save'):
    new_user = User(
      username=username,
      first_name=first_name,
      last_name=last_name,
      user_photo_url=user_photo_url if user_photo_url != '' else None,
      role=role,
      password=password
    )
    if new_user.create_user():
      st.success('User inserted successfully!')
    else:
      st.error('Error inserting user.')

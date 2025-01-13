import streamlit as st
from api.users import User

def create_page():
  ROLES = ['MEMBER', 'ADMIN']

  st.header('Edit User')

  # Get the username from the user
  user_username = st.text_input('Enter Username:')
  user = None

  # Check if the username is provided and retrieve the user
  if user_username:
    user = User(username=user_username).get_user_by_username()

  if user:
    # Display current user information in input boxes
    username = st.text_input('Username', user.username)
    role = st.selectbox("Role", ROLES, index=ROLES.index(user.role))
    first_name = st.text_input('First name', user.first_name)
    last_name = st.text_input('Last name', user.last_name)
    password = st.text_input('Password', type='password')
    user_photo_url = st.text_input('User photo url', user.user_photo_url)
    
    if st.button('Save Changes'):
      # Update the user with the new information
      user.username = username
      user.role = role
      user.first_name = first_name
      user.last_name = last_name
      user.password = password
      user.user_photo_url = user_photo_url

      if user.update_user():
        st.success('User updated successfully!')
      else:
        st.error('Error updating user.')
  elif user is not None:
    st.warning('Please enter a valid Username.')
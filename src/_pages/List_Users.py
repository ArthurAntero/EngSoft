import streamlit as st
from api.users import User
from globals import logged_user

def create_page():
  with open('src/globals.py', 'r') as file:
      exec(file.read())

  # Styles

  DIV_CONT = f'''
    padding: 2rem; 
    border-radius: 2rem; 
    color: black; 
    display: flex; 
    align-items: start; 
    justify-content: space-between; 
  '''

  TEXT = f'''
    color: black;
  '''

  USER_IMG = f'''
    height: 40%; 
    max-width: 35%; 
    margin-right: 1.25rem;
    color: black;
  '''

  USER_NO_IMG = f'''
    margin-top: auto;
    margin-bottom: auto;
    margin-right: 1.25rem;
    color: black;
  '''

  def get_book_color(book_index):
      colors = ["#FFDDC1", "#C2EABD", "#AED9E0", "#FFD3B5", "#D4A5A5"]
      return colors[book_index % len(colors)]

  # Page

  PAGE_TITLE = "List of Users"
  st.header(PAGE_TITLE)
  search_term = st.text_input("Search by Username, First or Last name or Role")

  users = User().get_users()

  if users:
    for index, user in enumerate(users):
      if (
        not search_term
        or search_term.lower() in user.username.lower()
        or search_term.lower() in user.first_name.lower()
        or search_term.lower() in user.last_name.lower()
        or search_term.lower() in user.role.lower()
      ):
        background_color = get_book_color(index)
        st.markdown(
          f'<div style="{(DIV_CONT)}  background-color: {background_color}">'
            f'<div>'
              f'<h3 style="{TEXT}">{user.first_name} {user.last_name}</h3>'
              f'<p style="{TEXT}">username: {user.username}</p>'
              f'<p style="{TEXT}">role: {user.role}</p>'
            f'</div>'
          f'<img src="{user.user_photo_url}" alt="User Photo" style="{USER_IMG if user.user_photo_url is not None else USER_NO_IMG}">'
          f'</div>',
          unsafe_allow_html=True
        )
        if logged_user["role"] == 'ADMIN' and user.id != logged_user['id']:
            st.text('')
            if st.button("Delete", key=user.id, use_container_width=True):
                User(id=user.id).delete_user()
                st.experimental_rerun()
        else:
          st.text('')
          st.text("You can't delete yourself")

        st.text('')

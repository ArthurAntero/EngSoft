import streamlit as st
from api.books import Book

def create_page():
    st.header('Add a New Book')

    isbn = st.number_input('isbn', min_value=0)
    title = st.text_input('Title')
    author = st.text_input('Author')
    description = st.text_input('description')
    category = st.selectbox("category", ['ROMANCE', 'COMEDY', 'DRAMA', 'SCIFI', 'HORROR'])
    date_acquisition = st.date_input('Date Acquisition')
    conservation_status = st.selectbox('Conservation Status', ['NEW', 'AVERAGE', 'OLD', 'DAMAGED'])
    physical_location = st.text_input('Physical Location')
    book_cover_url = st.text_input('Book Cover url')
    status = st.selectbox("Status", ['AVAILABLE', 'BORROWED'])

    if st.button('Save'):
        new_book = Book(
            int(isbn), 
            title, 
            author, 
            description, 
            category, 
            date_acquisition, 
            conservation_status,
            physical_location,
            book_cover_url,
            status,
        )
        if new_book.create_book():
            st.success('Book inserted successfully!')
        else:
            st.error('Error inserting book.')

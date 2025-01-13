import streamlit as st
from api.books import Book

def create_page():
    st.header('Edit Books')

    # Get the material ID from the user
    book_isbn = st.text_input('Enter Books ISBN:')
    book = None

    category_options = ['ROMANCE', 'COMEDY', 'DRAMA', 'SCIFI', 'HORROR']
    conservation_status_options = ['NEW', 'AVERAGE', 'OLD', 'DAMAGED']

    # Check if the material ID is provided and retrieve the material
    if book_isbn:
        book = Book(isbn=book_isbn).get_book_by_isbn()

    if book:
        # Display current material information in input boxes
        title = st.text_input('Title', book.title)
        author = st.text_input('Author', book.author)
        description = st.text_input('description', book.description)
        category = st.selectbox("category", category_options, index=category_options.index(book.category))
        date_acquisition = st.date_input('Date Acquisition', book.date_acquisition)
        conservation_status = st.selectbox('Conservation Status', conservation_status_options, index=conservation_status_options.index(book.conservation_status))
        physical_location = st.text_input('Physical Location', book.physical_location)
        book_cover_url = st.text_input('Book Cover url', book.book_cover_url)

        if st.button('Save Changes'):
            # Update the teaching material with the new information
            book = Book(
                int(book.isbn), 
                title, 
                author, 
                description, 
                category, 
                date_acquisition, 
                conservation_status,
                physical_location,
                book_cover_url,
                book.status,
            )
            if book.update_book():
                st.success('book edit successfully!')
            else:
                st.error('Error editing book.')
    else:
        st.warning('Please enter a valid Book ISBN.')

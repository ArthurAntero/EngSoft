import streamlit as st
from api.books import Book
from globals import logged_user

DIV_MAIN = f'''
    display: flex; 
    padding: 2rem; 
    color: black; 
    flex-direction: row;
    border-radius: 2rem;
'''

TITLE = f'''
    color: black; 
    word-wrap: normal; 
    max-width: 10rem;
'''

TEXT = f'''
    display: flex; 
    flex-direction: column; 
    flex-wrap: wrap; 
    margin-left: 20px; 
    word-wrap: break-word; 
    max-width: 20rem;
'''

IMAGE_STYLE = f'''
    height: 50%; 
    width: 35%; 
    align-self: center;
'''

def create_page():
    with open('src/globals.py', 'r') as file:
        exec(file.read())

    # Define a function to generate a unique color for each book
    def get_book_color(book_index):
        colors = ["#FFDDC1", "#C2EABD", "#AED9E0", "#FFD3B5", "#D4A5A5"]
        return colors[book_index % len(colors)]

    st.header('List of Books')

    # Get search term from user input
    search_term = st.text_input("Search by Title, Author, Category, ISBN, or Date Acquisition")

    books = Book().get_books()

    if books:
        for index, book in enumerate(books):
            # Filter books based on search term
            if (
                not search_term
                or search_term.lower() in str(book.isbn).lower()
                or search_term.lower() in book.title.lower()
                or search_term.lower() in book.author.lower()
                or search_term.lower() in book.description.lower()
                or search_term.lower() in book.category.lower()
                or search_term.lower() in str(book.date_acquisition).lower()
                or search_term.lower() in book.conservation_status.lower()
                or search_term.lower() in book.physical_location.lower()
                or search_term.lower() in book.status.lower()
                # Add more conditions as needed
            ):
                # Generate a unique color for each book
                background_color = get_book_color(index)

                # Limit the title to 23 characters
                if len(book.title) > 23:
                    display_title = f'{book.title[:23]}...'
                else:
                    display_title = book.title
                
                st.markdown(
                    f'<div style="{DIV_MAIN} background-color: {background_color};">'
                        f'<div style="flex: 1">'
                            f'<h2 style="{TITLE}">{display_title}</h2>'
                            f'<div style="{TEXT}">'
                                f'<p>ISBN: {book.isbn}</p>'
                                f'<p>Author: {book.author}</p>'
                                f'<p>Description: {book.description}</p>'
                                f'<p>Category: {book.category}</p>'
                                f'<p>Date Acquisition: {book.date_acquisition}</p>'
                                f'<p>Conservation Status: {book.conservation_status}</p>'
                                f'<p>Physical Location: {book.physical_location}</p>'
                                f'<p>Status: {book.status}</p>'
                            f'</div>'
                        f'</div>'
                        f'<img src="{book.book_cover_url}" alt="Book Cover" style="{IMAGE_STYLE}">'
                    f'</div>',
                    unsafe_allow_html=True
                )
                st.text('')
                if logged_user["role"] == 'ADMIN' and book.status == 'AVAILABLE':
                    if st.button("Delete", key=book.isbn, use_container_width=True):
                        Book(isbn=book.isbn).delete_book()
                        st.experimental_rerun()
                elif logged_user["role"] == 'ADMIN' and book.status != 'AVAILABLE':
                    st.text('You cannot delete a book that is on loan')

            st.text('')
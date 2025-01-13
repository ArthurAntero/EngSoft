from decouple import config
from globals import logged_user
import psycopg2

POSTGRES_DB = config('POSTGRES_DB')
POSTGRES_USER = config('POSTGRES_USER')
POSTGRES_PASSWORD = config('POSTGRES_PASSWORD')
POSTGRES_PORT = config('POSTGRES_PORT')

class Book:
    def __init__(
            self, 
            isbn = None, 
            title = None, 
            author = None, 
            description = None, 
            category = None, 
            date_acquisition = None, 
            conservation_status = None, 
            physical_location = None, 
            book_cover_url = None, 
            status = None
        ):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.description = description
        self.category = category
        self.date_acquisition = date_acquisition
        self.conservation_status = conservation_status
        self.physical_location = physical_location
        self.book_cover_url = book_cover_url
        self.status = status

    def _bd_connect(self):
        try:
            conn = psycopg2.connect(
                database=POSTGRES_DB,
                user=POSTGRES_USER,
                password=POSTGRES_PASSWORD,
                host="localhost",
                port=POSTGRES_PORT
            )
            return conn
        except Exception as e:
            print(f'Error connecting to the database: {e}')

    def create_book(self):
        with open('src/globals.py', 'r') as file:
            exec(file.read())

        if logged_user['role'] is None:
            print('You must be logged in to create a book')
            return False
        
        if logged_user["role"] != 'ADMIN':
            print('You do not have permission to create a book')
            return False
        
        try:
            conn = self._bd_connect()
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO Books (isbn, title, author, description, category, date_acquisition, conservation_status, physical_location, book_cover_url, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (
                    self.isbn, 
                    self.title, 
                    self.author, 
                    self.description,
                    self.category, 
                    self.date_acquisition, 
                    self.conservation_status, 
                    self.physical_location, 
                    self.book_cover_url, 
                    self.status, 
                )
            )
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f'Error inserting book: {e}')
            return False
        

    def update_book(self):
        with open('src/globals.py', 'r') as file:
            exec(file.read())

        if logged_user['role'] is None:
            print('You must be logged in to update a book')
            return False
        
        if logged_user["role"] != 'ADMIN':
            print('You do not have permission to update a book')
            return False
    
        try:
            conn = self._bd_connect()
            cur = conn.cursor()
            cur.execute(
                "UPDATE Books SET title = %s, author = %s, description = %s, category = %s, date_acquisition = %s, conservation_status = %s, physical_location = %s, book_cover_url = %s, status = %s WHERE isbn = %s",
                (
                    self.title, 
                    self.author, 
                    self.description,
                    self.category, 
                    self.date_acquisition, 
                    self.conservation_status, 
                    self.physical_location, 
                    self.book_cover_url, 
                    self.status, 
                    self.isbn
                )
            )
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f'Error updating book: {e}')
            return False

    def delete_book(self):
        with open('src/globals.py', 'r') as file:
            exec(file.read())

        if logged_user['role'] is None:
            print('You must be logged in to delete a book')
            return False
        
        if logged_user["role"] != 'ADMIN':
            print('You do not have permission to delete a book')
            return False
    
        try:
            conn = self._bd_connect()
            cur = conn.cursor()
            cur.execute(
                "DELETE FROM Books WHERE isbn = %s",
                (self.isbn,)
            )
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f'Error deleting book: {e}')
            return False

    def get_books(self):
        try:
            conn = self._bd_connect()
            cur = conn.cursor()
            cur.execute('SELECT * FROM Books')
            books_data = cur.fetchall()
            conn.close()

            books = []
            for book_data in books_data:
                book = Book(*book_data)
                books.append(book)

            books.sort(key=lambda x: x.title)
            return books
        except Exception as e:
            print(f'Error fetching books: {e}')

    def get_book_by_isbn(self):

        try:
            conn = self._bd_connect()
            cur = conn.cursor()
            cur.execute('SELECT * FROM Books WHERE isbn = %s', (self.isbn,))
            book_data = cur.fetchone()
            conn.close()

            if book_data:
                user = Book(*book_data)
                return user

        except Exception as e:
            print(f'Error fetching books: {e}')

    def get_available_books(self):

        try:
            conn = self._bd_connect()
            cur = conn.cursor()
            cur.execute("SELECT * FROM Books WHERE status = 'AVAILABLE'")
            available_books = cur.fetchall()
            conn.close()
            
            books = []
            for book_data in available_books:
                book = Book(*book_data)
                books.append(book)

            return books
        except Exception as e:
            print(f'Error fetching available books: {e}')
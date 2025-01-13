import streamlit as st
from datetime import datetime, timedelta
from api.users import User
from api.loan import Loan
from api.books import Book
from globals import logged_user

DIV_MAIN = f'''
    display: flex; 
    padding: 2rem; 
    color: black; 
    flex-direction: row;
    border-radius: 2rem;
'''

TEXT = f'''
    display: flex; 
    flex-direction: column; 
    flex-wrap: wrap; 
    margin-left: 20px; 
    word-wrap: break-word; 
    max-width: 20rem;
'''

def create_page():
    with open('src/globals.py', 'r') as file:
        exec(file.read())

    user_role = logged_user["role"]
    user_id = 0
    if user_role is not None:
        user_id = logged_user["id"]

    loans = Loan().get_all_loans()

    if user_role == "MEMBER":
        loans = [loan for loan in loans if loan.id_user == logged_user["id"]]

    def get_loan_color(loan_index):
        colors = ["#FFDDC1", "#C2EABD", "#AED9E0", "#FFD3B5", "#D4A5A5"]
        return colors[loan_index % len(colors)]

    st.header('List Loans')

    search_term = st.text_input("Search by id, description, category, date acquisition, serie number, etc.")

    if loans:
        for index, loan in enumerate(loans):
            loan_first_name = User(loan.id_user).get_user_by_id().first_name
            if loan.id_book is not None:
                book_name = Book(loan.id_book).get_book_by_isbn().title
            if (
                not search_term
                or search_term.lower() in str(loan.id).lower()
                or search_term.lower() in str(loan.id_book).lower()
                or search_term.lower() in str(loan.id_material).lower()
                or search_term.lower() in str(loan.id_user).lower()
                or search_term.lower() in str(loan.loan_date).lower()
                or search_term.lower() in str(loan.expected_return_date).lower()
                or search_term.lower() in loan.status.lower()
                or search_term.lower() in loan_first_name.lower()
                or search_term.lower() in book_name.lower()
            ):
                background_color = get_loan_color(index)

                if user_role == "ADMIN":
                    if loan.id_book is None: # Material Didático
                        st.markdown(
                            f'<div style="{DIV_MAIN} background-color: {background_color};">'
                                f'<div style="flex: 1; padding-right: 10px;">'
                                    f'<h2 style="color: black">ID: {loan.id}</h2>'
                                    f'<div style="{TEXT}">'
                                        f'<p>Status: {loan.status}</p>'
                                        f'<p>Loan Date: {loan.loan_date}</p>'
                                        f'<p>Expected Return Date: {loan.expected_return_date}</p>'
                                        f'<p>Teaching Material ID: {loan.id_material}</p>'
                                        f'<p>User ID: {loan.id_user}</p>'
                                        f'<p>User First Name: {loan_first_name}</p>'
                                    f'</div>'
                                f'</div>'
                            f'</div>',
                            unsafe_allow_html=True
                        )
                        st.text('')
                    else: # Livro
                        st.markdown(
                            f'<div style="{DIV_MAIN} background-color: {background_color};">'
                                f'<div style="flex: 1; padding-right: 10px;">'
                                    f'<h2 style="color: black">ID: {loan.id}</h2>'
                                    f'<div style="{TEXT}">'
                                        f'<p>Status: {loan.status}</p>'
                                        f'<p>Loan Date: {loan.loan_date}</p>'
                                        f'<p>Expected Return Date: {loan.expected_return_date}</p>'
                                        f'<p>Book ID: {loan.id_book}</p>'
                                        f'<p>Book Name: {book_name}</p>'
                                        f'<p>User ID: {loan.id_user}</p>'
                                        f'<p>User First Name: {loan_first_name}</p>'
                                    f'</div>'
                                f'</div>'
                            f'</div>',
                            unsafe_allow_html=True
                        )
                        st.text('')
                        
                    st.text('')
                    if loan.status == "IN_PROGRESS":

                        if st.button("Postpone 1 week", key=loan.id, use_container_width=True):
                            Loan(id=loan.id, status="IN_PROGRESS", expected_return_date=(datetime.strptime(f'{loan.expected_return_date}', '%Y-%m-%d') + timedelta(days=7))).update_return_date()
                            st.experimental_rerun()
                        
                        if st.button("Finish", key=loan.id*0.1, use_container_width=True):
                            Loan(id=loan.id, status="COMPLETED").update_loan_status()
                            st.experimental_rerun()
                    else:
                        st.text('This Loan is Completed')

                        st.text('')
                elif user_role == "MEMBER" and user_id == loan.id_user:
                    if loan.id_book is None: # Material Didático
                        st.markdown(
                            f'<div style="{DIV_MAIN} background-color: {background_color};">'
                                f'<div style="flex: 1; padding-right: 10px;">'
                                    f'<h2 style="color: black">ID: {loan.id}</h2>'
                                    f'<div style="{TEXT}">'
                                        f'<p>Status: {loan.status}</p>'
                                        f'<p>Loan Date: {loan.loan_date}</p>'
                                        f'<p>Expected Return Date: {loan.expected_return_date}</p>'
                                        f'<p>Teaching Material ID: {loan.id_material}</p>'
                                        f'<p>User ID: {loan.id_user}</p>'
                                        f'<p>User First Name: {loan_first_name}</p>'
                                    f'</div>'
                                f'</div>'
                            f'</div>',
                            unsafe_allow_html=True
                        )
                        st.text('')
                        if loan.status == "IN_PROGRESS":
                            if st.button("Postpone 1 week", key=loan.id, use_container_width=True):
                                Loan(id=loan.id, status="IN_PROGRESS", expected_return_date=(datetime.strptime(f'{loan.expected_return_date}', '%Y-%m-%d') + timedelta(days=7))).update_return_date()
                                st.experimental_rerun()

                        st.text('')
                    else: # Livro
                        book_name = Book(loan.id_book).get_book_by_isbn().title
                        st.markdown(
                            f'<div style="{DIV_MAIN} background-color: {background_color};">'
                                f'<div style="flex: 1; padding-right: 10px;">'
                                    f'<h2 style="color: black">ID: {loan.id}</h2>'
                                    f'<div style="{TEXT}">'
                                        f'<p>Status: {loan.status}</p>'
                                        f'<p>Loan Date: {loan.loan_date}</p>'
                                        f'<p>Expected Return Date: {loan.expected_return_date}</p>'
                                        f'<p>Book ID: {loan.id_book}</p>'
                                        f'<p>Book Name: {book_name}</p>'
                                        f'<p>Library User ID: {loan.id_user}</p>'
                                        f'<p>Library User First Name: {loan_first_name}</p>'
                                    f'</div>'
                                f'</div>'
                            f'</div>',
                            unsafe_allow_html=True
                        )
                        st.text('')
    
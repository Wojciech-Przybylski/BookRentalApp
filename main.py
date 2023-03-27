from pony.orm import db_session, delete

import models
from models import Book


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def add_book():
    book_title = input("Insert the book title: ")
    book_author = input("Insert the book author: ")
    book_genre = input("Insert the book genre: ")
    book_rating = input("Insert the book rating: ")
    book_price = input("Insert the book price: ")
    Book.add_book(book_title, book_author, book_genre, book_rating, book_price)


def delete_book():
    book_title = input("Insert the book title: ")
    Book.delete_book(book_title)


def view_all_books():
    for b in Book.select(lambda b: b.book_title):
        print(f"{b.book_title} - {b.book_author}")


def view_all_available_books():
    for b in Book.select(lambda b: b.book_availability == "yes"):
        print(f"{b.book_title} - {b.book_author}")


def view_rented_books():
    for b in Book.select(lambda b: b.book_availability == "no"):
        print(f"{b.book_title} - {b.book_author}")


def search_genre():
    for b in Book.select(lambda b: b.book_genre):
        print(f"--Choose from the list of genres available below--"
              f"{b.book_genre}")


if __name__ == '__main__':
    with db_session:
        # admin view
        admin_selector = input("""--AdminView--
Welcome to our library! Select an action.
Add - Add new book
Del - Delete an existing book
VB - View all books
VA - View available books
VR - View rented books
SG - Search by genre
""")
        if admin_selector.lower() == "add":
            add_book()
        elif admin_selector.lower() == "del":
            delete_book()
        elif admin_selector.lower() == "vb":
            print("--Here are all books we rent--")
            view_all_books()
        elif admin_selector.lower() == "va":
            print("--Here are books that are currently available--")
            view_all_available_books()
        elif admin_selector.lower() == "vr":
            print("--Here are books that are currently rented--")
            view_rented_books()
        elif admin_selector.lower() == "sg":
            search_genre()

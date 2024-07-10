# lib/helpers.py

from models.patron import Patron
from models.book import Book
from models.__init__ import CURSOR, CONN


def list_patrons():
    patrons = Patron.get_all()
    for i, patron in enumerate(patrons, start=1):
        print(f"{i}. {patron.first_name} {patron.last_name}, {patron.age}")


def list_books(patron):
    books = patron.books()
    if len(books) > 0:
        for i, book in enumerate(books, start=1):
            print(f' {i}. {book.title}')
    else:
        print("")
        print(f'{patron.first_name} currently has no books.')


def print_book_details(book):
    print("")
    print(f'Title: {book.title}')
    print(f'Author: {book.author}')
    print(f'Pages: {book.pages}')
    print(f'Description: {book.description}')


def update_patron(patron):
    first_name = input("Enter new first name (if first name hasn't changed, leave it blank and press <ENTER>): ")
    last_name = input("Enter new last name (if last name hasn't changed, leave it blank and press <ENTER>): ")
    age = input("Enter new age (if age hasn't changed, leave it blank and press <ENTER>): ")
    if first_name == "":
        first_name = patron.first_name
    if last_name == "":
        last_name = patron.last_name
    if age == "":
        age = patron.age
    patron.update(first_name, last_name, age)


def update_book(book, patron):
    title = input("Enter new title (if title hasn't changed, leave it blank and press <ENTER>): ")
    author = input("Enter new author (if author hasn't changed, leave it blank and press <ENTER>): ")
    pages = input("Enter new page total (if pages haven't changed, leave it blank and press <ENTER>): ")
    description = input("Enter new description (if description hasn't changed, leave it blank and press <ENTER>): ")
    if title == "":
        title = book.title
    if author == "":
        author = book.author
    if pages == "":
        pages = book.pages
    if description == "":
        description = book.description
    book.update(title, author, int(pages), description, patron.id)
    
        
def add_new_patron():
    first_name = input("Enter the patron's first name: ")
    last_name = input("Enter the patron's last name: ")
    age = int(input("Enter the patron's age: "))
    Patron.create(first_name, last_name, age)


def add_new_book(patron):
    title = input("Enter the book's title: ")
    if title == "":
            print("Please enter a valid title.")
    author = input("Enter the book's author: ")
    pages = input("Enter the number of pages: ")
    description = input("Enter a brief description: ")
    Book.create(title, author, int(pages), description, patron.id)


def delete_patron(patron):
    patron.delete()


def delete_book(book):
    book.delete()


def exit_program():
    print("")
    print("Goodbye!")
    print("")
    exit()


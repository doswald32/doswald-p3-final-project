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


def update_patron():
    id_ = input("Enter the patron's id: ")
    if patron := Patron.find_by_id(id_):
        try:
            first_name = input("Enter patron's new first name: ")
            patron.first_name = first_name
            last_name = input("Enter patron's new last name: ")
            patron.last_name = last_name
            age = int(input("Enter patron's new age: "))
            patron.age = age
            patron.update()
            print(f'Success: {patron}')
        except Exception as exc:
            print("Error updating patron: ", exc)
    else:
        print(f'Patron {id_} not found')


def update_book(book):
    title = input("Enter new title (if title hasn't changed, leave it blank and press <ENTER>): ")
    author = input("Enter new title (if author hasn't changed, leave it blank and press <ENTER>): ")
    pages = input("Enter new title (if pages haven't changed, leave it blank and press <ENTER>): ")
    description = input("Enter new title (if description hasn't changed, leave it blank and press <ENTER>): ")
    if title == "":
        title = book.title
    if author == "":
        author = book.author
    if pages == "":
        pages = book.pages
    if description == "":
        description = book.description
    
        
def add_new_patron():
    first_name = input("Enter the patron's first name: ")
    last_name = input("Enter the patron's last name: ")
    age = int(input("Enter the patron's age: "))
    Patron.create(first_name, last_name, age)

def add_new_book(patron):
    title = input("Enter the book's title: ")
    author = input("Enter the book's author: ")
    pages = int(input("Enter the number of pages: "))
    description = input("Enter a brief description: ")
    Book.create(title, author, pages, description, patron.id)


# def display_book_info(p_choice, b_choice):
#     sql = """
#         SELECT * 
#         FROM books
#         WHERE patron_id = ?
#     """
#     rows = CURSOR.execute(sql, (p_choice,)).fetchall()
#     i = int(b_choice) - 1
#     print("")
#     print(f"Title: {rows[i][1]}")
#     print(f"Author: {rows[i][2]}")
#     print(f"Pages: {rows[i][3]}")
#     print(f"Description: {rows[i][4]}")
#     print(f"ID: {rows[i][0]}")
#     print("")
#     book_id = int(rows[i][0])
#     return book_id



def delete_patron(p_choice):
    sql = """   
        SELECT *
        FROM books
        WHERE patron_id = ?
    """
    sql2 = """
        DELETE FROM patrons
        WHERE id = ?
    """
    rows = CURSOR.execute(sql, (p_choice,)).fetchall()
    for row in rows:
        book = Book.instance_from_db(row)
        book.delete()
    CURSOR.execute(sql2, (p_choice,))
    CONN.commit()
    print("")
    print("Patron successfully deleted")
    print("")
    list_patrons()


def delete_book(p_choice, b_choice):
    sql = """
        SELECT *
        FROM books
        WHERE patron_id = ?
    """
    rows = CURSOR.execute(sql, (p_choice,)).fetchall()
    book = Book.instance_from_db(rows[int(b_choice) - 1])
    return book


# def input_converter():
#     rows = CURSOR.execute("SELECT * FROM patrons")
#     return rows
#     patron = rows[int(p_choice) - 1]
#     book = CURSOR.execute("SELECT * FROM books WHERE patron_id = ?", (patron.id,))


def exit_program():
    print("")
    print("Goodbye!")
    print("")
    exit()


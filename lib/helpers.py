# lib/helpers.py

from models.patron import Patron
from models.book import Book
# from cli import books_menu, patron_menu
from models.__init__ import CURSOR, CONN


def list_patrons():
    patrons = Patron.get_all()
    print("**********")
    print("")
    for i, patron in enumerate(patrons, start=1):
        print(f"{i}. {patron.first_name} {patron.last_name}, {patron.age}")
    print("")
    print("**********")
    print("")


# def patron_details():
#     try:
#         id = int(input("Enter the ID of the patron: "))
#         patron = Patron.find_by_id(id)
#         if patron:
#             print("**********")
#             print("")
#             print(f"{patron.id}. {patron.first_name} {patron.last_name}, {patron.age}")
#             print("")
#             print("**********")
#             print("")
#         else:
#             print("Patron not found.")
#     except ValueError:
#         print("Invalid ID. Please enter valid integer.")


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

def list_books(patron):
    # sql = """
    #     SELECT *
    #     FROM books
    #     WHERE patron_id = ?
    # """
    # breakpoint()
    books = patron.books()
    # rows = CURSOR.execute(sql, (p_choice,)).fetchall()
    if len(books) > 0:
        for i, book in enumerate(books, start=1):
            print(f' {i}. {book.title}')
        books_menu(p_choice)
    else:
        print("")
        print("Patron has no books")
        print("")
        no_books_menu(p_choice)
        


def add_new_patron():
    first_name = input("Enter the patron's first name: ")
    last_name = input("Enter the patron's last name: ")
    age = int(input("Enter the patron's age: "))
    Patron.create(first_name, last_name, age)


def display_book_info(p_choice, b_choice):
    sql = """
        SELECT * 
        FROM books
        WHERE patron_id = ?
    """
    rows = CURSOR.execute(sql, (p_choice,)).fetchall()
    i = int(b_choice) - 1
    print("")
    print(f"Title: {rows[i][1]}")
    print(f"Author: {rows[i][2]}")
    print(f"Pages: {rows[i][3]}")
    print(f"Description: {rows[i][4]}")
    print(f"ID: {rows[i][0]}")
    print("")
    book_id = int(rows[i][0])
    return book_id


def print_choice_name(p_choice):
    sql = """
        SELECT * 
        FROM patrons
    """
    index = int(p_choice) - 1
    rows = CURSOR.execute(sql).fetchall()
    print("")
    print(f'{rows[index][1]} {rows[index][2]}')
    print("")


def add_new_book(title, author, pages, description, patron_id):
    Book.create(title, author, pages, description, patron_id)


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


def update_book(title, author, pages, description, p_choice, b_choice):
    sql = """
        SELECT * 
        FROM books 
        WHERE patron_id = ?
    """
    rows = CURSOR.execute(sql, (p_choice,)).fetchall()
    index = int(b_choice) - 1
    if title == "":
        title = rows[index][1]
    if author == "":
        author = rows[index][2]
    if pages == "":
        pages = rows[index][3]
    if description == "":
        description = rows[index][4]
    book = Book.instance_from_db(rows[index])
    breakpoint()
    return book


def exit_program():
    print("")
    print("Goodbye!")
    print("")
    exit()


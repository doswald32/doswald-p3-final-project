# lib/helpers.py

from models.patron import Patron
from models.book import Book
from models.__init__ import CURSOR, CONN


def list_patrons():
    patrons = Patron.get_all()
    print("**********")
    print("")
    for patron in patrons:
        print(f"Patron ID: {patron.id} {patron.first_name} {patron.last_name}, {patron.age}")
    print("")
    print("**********")
    print("")


def patron_details():
    try:
        id = int(input("Enter the ID of the patron: "))
        patron = Patron.find_by_id(id)
        if patron:
            print("**********")
            print("")
            print(f"{patron.id}. {patron.first_name} {patron.last_name}, {patron.age}")
            print("")
            print("**********")
            print("")
        else:
            print("Patron not found.")
    except ValueError:
        print("Invalid ID. Please enter valid integer.")

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

def list_books(p_choice, books_menu, no_book_menu):
    sql = """
        SELECT *
        FROM books
        WHERE patron_id = ?
    """
    rows = CURSOR.execute(sql, (p_choice,)).fetchall()
    if rows:
        for i, row in enumerate(rows, start=1):
            print(f"{i}. {row[1]}")
        books_menu(p_choice)
    else:
        print("")
        print("Patron has no books")
        print("")
        no_book_menu(p_choice)
        


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
        WITH NumberedRows AS (
            SELECT *, ROW_NUMBER() OVER (ORDER BY id) AS RowNum
            FROM patrons
        )
        SELECT * 
        FROM patrons
        WHERE id = ?
    """
    print(p_choice)
    row = CURSOR.execute(sql, (p_choice,)).fetchone()
    print("")
    print(f"{row[1]} {row[2]}")
    print("")


def add_new_book(title, author, pages, description, patron_id):
    Book.create(title, author, pages, description, patron_id)


def delete_patron(p_choice):
    sql = """
        DELETE FROM patrons
        WHERE id = ?
    """
    CURSOR.execute(sql, (p_choice,))
    CONN.commit()
    print("")
    print("Patron successfully deleted")
    print("")
    list_patrons()


def delete_book(p_choice):
    sql = """
        SELECT * 
        FROM books
        WHERE patron_id = ?
    """
    print(p_choice)
    rows = CURSOR.execute(sql, (p_choice,)).fetchall()
    print(type(rows[1]))


def exit_program():
    print("")
    print("Goodbye!")
    print("")
    exit()


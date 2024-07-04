# lib/helpers.py

from models.patron import Patron
from models.book import Book
from models.__init__ import CURSOR, CONN
import ipdb


def list_patrons():
    patrons = Patron.get_all()
    print("**********")
    print("")
    for patron in patrons:
        print(f"{patron.id}. {patron.first_name} {patron.last_name}, {patron.age}")
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

def list_books(choice):
    sql = """
        SELECT *
        FROM books
        WHERE id = ?
    """
    rows = CURSOR.execute(sql, (choice,)).fetchall()
    for i, row in enumerate(rows, start=1):
    	print(f"{i}. {row}")



def exit_program():
    print("Goodbye!")
    exit()


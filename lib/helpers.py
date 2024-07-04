# lib/helpers.py

from models.patron import Patron
from models.book import Book
from models.__init__ import CURSOR, CONN


def list_patrons():
    patrons = Patron.get_all()
    print("**********")
    for patron in patrons:
        print(f"{patron.id}. {patron.first_name} {patron.last_name}, {patron.age}")
    print("**********")
    print("")


def patron_details():
    try:
        id = int(input("Enter the ID of the patron: "))
        patron = Patron.find_by_id(id)
        if patron:
            print("**********")
            print(f"{patron.id}. {patron.first_name} {patron.last_name}, {patron.age}")
            print("**********")
            print("")
        else:
            print("Patron not found.")
    except ValueError:
        print("Invalid ID. Please enter valid integer.")


def exit_program():
    print("Goodbye!")
    exit()


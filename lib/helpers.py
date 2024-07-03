# lib/helpers.py

from models.patron import Patron
from models.__init__ import CURSOR, CONN

def list_patrons():
    patrons = Patron.get_all()
    print("**********")
    for patron in patrons:
        print(f"{patron.id}. {patron.first_name} {patron.last_name}, {patron.age}")
    print("**********")
    print("")

def exit_program():
    print("Goodbye!")
    exit()


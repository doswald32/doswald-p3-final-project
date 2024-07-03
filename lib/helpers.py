# lib/helpers.py

from models.patron import Patron
from models.__init__ import CURSOR, CONN

def list_patrons():
    patrons = Patron.get_all()
    for patron in patrons:
        print(patron)

def exit_program():
    print("Goodbye!")
    exit()


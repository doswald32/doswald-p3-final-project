# lib/helpers.py

from models.patron import Patron
from models.__init__ import CURSOR, CONN

def access_patrons():
    patrons = CURSOR.execute("SELECT * FROM patrons")
    print(patrons)


def exit_program():
    print("Goodbye!")
    exit()


from models.patron import Patron
from models.book import Book
from models.__init__ import CURSOR, CONN 

def seed_database():
    Patron.drop_table()
    Patron.create_table()
    Book.drop_table()
    Book.create_table()

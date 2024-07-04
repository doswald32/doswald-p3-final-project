from models.patron import Patron
from models.book import Book
from models.__init__ import CURSOR, CONN 

def seed_database():
    Patron.drop_table()
    Patron.create_table()
    Book.drop_table()
    Book.create_table()

    Steve_oswald = Patron.create("Steve", "Oswald", 62)
    Carol_oswald = Patron.create("Carol", "Oswald", 62)
    Book.create("Harry Potter 1", "JK Rowling", 305, "A young wizard confronts his dark past.", Steve_oswald.id)
    Book.create("Harry Potter 2", "JK Rowling", 287, "The story continues.", Steve_oswald.id)
    Book.create("The Tipping Point", "Malcom Gladwell", 256, "What makes a marketing campaign successful?", Carol_oswald.id)
    Book.create("The DaVinci Code", "Dan Brown", 500, "It's a good one!", Carol_oswald.id)


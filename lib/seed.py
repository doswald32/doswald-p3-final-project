from models.patron import Patron
from models.book import Book

def seed_database():
    Patron.drop_table()
    Patron.create_table()
    Book.drop_table()
    Book.create_table()

    Steve_oswald = Patron.create("Steve", "Oswald", 62)
    Carol_oswald = Patron.create("Carol", "Oswald", 62)
    Dan_oswald = Patron.create("Dan", "Oswald", 33)
    David_oswald = Patron.create("David", "Oswald", 34)
    HP1 = Book.create("Harry Potter 1", "JK Rowling", 305, "A young wizard confronts his dark past.", Steve_oswald.id)
    HP2 = Book.create("Harry Potter 2", "JK Rowling", 287, "The story continues.", Steve_oswald.id)
    TTP = Book.create("The Tipping Point", "Malcom Gladwell", 256, "What makes a marketing campaign successful?", Carol_oswald.id)
    TDC = Book.create("The DaVinci Code", "Dan Brown", 500, "It's a good one!", Carol_oswald.id)
    LOTR = Book.create("The Lord of the Rings", "J.R.R. Tolkein", 385, "The fate of middle earth rests with two young hobbies.", Dan_oswald.id)
    print("Database seeded.")


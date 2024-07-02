from __init__ import CURSOR, CONN

class Patron:

    def __init__(self, first_name, last_name, birth_date, books=None):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.books = books

    @classmethod
    def create_table(cls):
        """ Create a new table to keep track of attributes associated with various Patron instances """
        sql = """
            CREATE TABLE IF NOT EXISTS patrons (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            birth_date TEXT,
            )
        """
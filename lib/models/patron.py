from . import CURSOR, CONN

class Patron:

    def __init__(self, first_name, last_name, birth_date, books=None):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.books = books

    def __repr__(self):
        return f"<Patron {self.id}: {self.last_name}, {self.first_name}  {self.birth_date}>"

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
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table the hosts instances of the Patron class """
        sql = """
            DROP TABLE IF EXISTS patrons;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row in the patrons table with name and DOB of the Patron instance. Update ID attribute using primary key of row """
        sql = """
            INSERT INTO patrons (first_name, last_name, birth_date)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.first_name, self.last_name, self.birth_date))
        CONN.commit()

        self.id = CURSOR.lastrowid
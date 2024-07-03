from . import CURSOR, CONN

class Patron:

    all = {}

    def __init__(self, first_name, last_name, age, id=None, books=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.id = id
        self.books = books

    def __repr__(self):
        return f"<Patron ID {self.id}: {self.last_name}, {self.first_name}   Age: {self.age}>"
    
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, value):
        if isinstance(value, str) and len(value) >= 1:
            self._first_name = value
        else:
            raise TypeError("First name must be a string with at least 1 character.")


    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, value):
        if isinstance(value, str) and len(value) >= 1:
            self._last_name = value
        else:
            raise TypeError("Last name must be a string with at least 1 character.")


    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if isinstance(value, int) and value >= 18:
            self._age = value
        else:
            raise TypeError("Age must be an integer greater than or equal to 18.")


    @classmethod
    def create_table(cls):
        """ Create a new table to keep track of attributes associated with various Patron instances """
        sql = """
            CREATE TABLE IF NOT EXISTS patrons (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            age TEXT
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
            INSERT INTO patrons (first_name, last_name, age)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.first_name, self.last_name, self.age))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, first_name, last_name, age):
        """ Create an instance of Patron and save its attributes to the database """
        breakpoint()
        patron = cls(first_name, last_name, age)
        breakpoint()
        patron.save()
        breakpoint()
        return patron
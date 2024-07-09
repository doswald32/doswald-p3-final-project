from . import CURSOR, CONN

class Patron:

    all = {}


    def __init__(self, first_name, last_name, age, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.id = id


    def __repr__(self):
        return f"<Patron ID {self.id}: {self.last_name}, {self.first_name}   Age: {self.age}>"
    

    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, value):
        if isinstance(value, str) and len(value):
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


    def books(self):
        from models.book import Book
        sql = """
            SELECT * FROM books
            WHERE patron_id = ?
        """
        print(f"Patron ID: {self.id}")
        CURSOR.execute(sql, (self.id,))
        rows = CURSOR.fetchall()
        # print(f"Rows: {rows}")
        return [Book.instance_from_db(row) for row in rows]


    @classmethod
    def create_table(cls):
        """ Create a new table to keep track of attributes associated with various Patron instances """
        sql = """
            CREATE TABLE IF NOT EXISTS patrons (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            age INTEGER
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
        """ Insert a new row in the patrons table with name and DOB of the Patron instance. Update ID attribute using primary key of row and save the object to the Patron dictionary """
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
        patron = cls(first_name, last_name, age)
        patron.save()
        return patron


    def update(self):
        """ Updates table row associated with the Patron instance, not the object itself. """
        sql = """
            UPDATE patrons 
            SET first_name = ?, last_name = ?, age = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.first_name, self.last_name, self.age, self.id))
        CONN.commit()

    
    def delete(self):
        """ Delete database row associated with Patron instance """
        sql = """
            DELETE FROM patrons
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None


    @classmethod
    def instance_from_db(cls, row):
        """ Return a Patron object using data from the table """
        patron = cls.all.get(row[0])
        # age = int(row[3])
        if patron:
            patron.first_name = row[1]
            patron.last_name = row[2]
            patron.age = row[3]
        else:
            patron = cls(row[1], row[2], row[3])
            patron.id = row[0]
            cls.all[patron.id] = patron
        return patron
    
    
    
    @classmethod
    def get_all(cls):
        """ Return a list of patrons from the Patrons table """
        sql = """
            SELECT * FROM patrons
        """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    
    @classmethod
    def find_by_id(cls, id):
        """ Return a Patron object associated with the table row that matches the id """
        sql = """
            SELECT *
            FROM patrons
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    

    @classmethod
    def find_by_first_name(cls, first_name):
        sql = """
            SELECT * 
            FROM patrons 
            WHERE first_name = ?
        """
        row = CURSOR.execute(sql, (first_name,)).fetchone()
        print(type(row))
        return cls.instance_from_db(row) if row else None
    

    @classmethod
    def table_length(cls):
        sql = """
            SELECT *
            FROM patrons
        """
        rows = CURSOR.execute(sql).fetchall()
        return int(len(rows))
    

        
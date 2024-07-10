from . import CURSOR, CONN
from models.patron import Patron

class Book():

    all = {}


    def __init__(self, title, author, pages, description, patron_id, id=None):
        self.title = title
        self.author = author
        self.pages = pages
        self.description = description
        self.patron_id = patron_id
        self.id = id


    def __repr__(self):
        return (
            f"<{self.title}, by {self.author}>\n"
            f"<Patron ID: {self.patron_id}>\n"
        )


    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if isinstance(value, str) and len(value):
            self._title = value
        else: 
            raise TypeError("Title must be a string with at least 1 character.")
        
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if isinstance(value, str) and len(value):
            self._author = value
        else:
            raise TypeError("Author must be a string with at least 1 character.")
        
    
    @property
    def pages(self):
        return self._pages
    
    @pages.setter
    def pages(self, value):
        if isinstance(value, int):
            self._pages = value
        else:
            raise TypeError("Pages must be an integer between 1-10000.")
    

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 1000:
            self._description = value
        else:
            raise TypeError("Description must be a string between 1 and 1000 characters.")
        

    @property
    def patron_id(self):
        return self._patron_id
    
    @patron_id.setter
    def patron_id(self, patron_id):
        if type(patron_id) is int and Patron.find_by_id(patron_id):
            self._patron_id = patron_id
        else:
            raise ValueError("patron_id must reference a patron in the database")


    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            pages INTEGER,
            description TEXT,
            patron_id INTEGER
            )
        """
        CURSOR.execute(sql)
        CONN.commit()


    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS books;
        """
        CURSOR.execute(sql)
        CONN.commit()

        
    def save(self):
        sql = """
            INSERT INTO books (title, author, pages, description, patron_id)
            VALUES (?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.title, self.author, self.pages, self.description, self.patron_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    
    @classmethod
    def create(cls, title, author, pages, description, patron_id):
            book = cls(title, author, pages, description, patron_id)
            book.save()
            return book
    

    def update(self, title, author, pages, description, patron_id):
        sql = """
            UPDATE books
            SET title = ?, author = ?, pages = ?, description = ?, patron_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (title, author, pages, description, patron_id, self.id))
        CONN.commit()


    def delete(self):
        sql = """
            DELETE FROM books
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None


    @classmethod
    def instance_from_db(cls, row):
        book = cls.all.get(row[0])
        if book:
            book.title = row[1]
            book.author = row[2]
            book.pages = row[3]
            book.description = row[4]
            book.patron_id = row[5]
        else:
            book = cls(row[1], row[2], row[3], row[4], row[5])
            book.id = row[0]
            cls.all[book.id] = book
        return book
    

    @classmethod
    def get_all(cls):
        sql = """
            SELECT * 
            FROM books
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM books
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    

    @classmethod
    def find_by_title(cls, title):
        sql = """
            SELECT *
            FROM books
            WHERE title = ?
        """
        row = CURSOR.execute(sql, (title,)).fetchone()
        return cls.instance_from_db(row) if row else None
    

    @classmethod
    def table_length(cls):
        sql = """
            SELECT *
            FROM books
        """
        rows = CURSOR.execute(sql).fetchall()
        return int(len(rows))
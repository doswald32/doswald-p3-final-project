from __init__ import CURSOR, CONN

class Book():

    all = {}


    def __init__(self, title, author, pages, description):
        self.title = title
        self.author = author
        self.pages = pages
        self.description = description


    def __repr__(self):
        return f"<{self.title}, by {self.author}>"


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
        if isinstance(value, int) and 1 >= len(value) <=10000:
            self._pages = value
        raise TypeError("Pages must be an integer between 1-10000.")
    

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        if isinstance(value, str) and 1 >= len(value) <= 1000:
            self._description = value
        else:
            raise TypeError("Description must be a string between 1 and 1000 characters.")
        

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            pages INTEGER,
            description TEXT
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
            INSERT INTO books (title, author, pages, description)
            VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.title, self.author, self.pages, self.description))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    
    @classmethod
    def create(cls, title, author, pages, description):
        book = cls(title, author, pages, description)
        book.save()
        return book
    

    def update(self):
        sql = """
            UPDATE books
            SET title = ?, author = ?, pages = ?, description = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.title, self.author, self.pages, self.description, self.id))
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
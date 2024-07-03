from . import CURSOR, CONN

class Book():

    def __init__(self, title, author, pages, description):
        self.title = title
        self.author = author
        self.pages = pages
        self.description = description

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if isinstance(value, str) and len(value) >= 1:
            self._title = value
        else: 
            raise TypeError("Title must be a string with at least 1 character.")
        
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if isinstance(value, str) and len(value) >= 1:
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
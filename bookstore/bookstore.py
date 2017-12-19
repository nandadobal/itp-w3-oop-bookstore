class Bookstore(object):
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []
    #adds books to the bookstore    
    def add_book(self, a_book):
        self.books.append(a_book)
        self.authors.append(a_book.author)
    #get all books
    def get_books(self):
        return self.books
    #get books by author or title     
    def search_books(self, author=None, title=None):
        results = []
        if title and author:
            for book in self.books:
                if title.lower() in book.title.lower():
                    results.append(book)
            return restuls
        if title == None:
            for book in self.books:
                if book.author == author:
                    results.append(book)
            return results
        if author == None:
            for book in self.books:
                if title.lower() in book.title.lower():
                    results.append(book)
            return results


class Author(object):
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.books =[]
    def get_books(self):
        return self.books
        


class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        #adds book object to Author object's list of books 
        self.author.books.append(self)




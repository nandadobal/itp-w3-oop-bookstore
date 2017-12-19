from .bookstore import *

#create bookstore with name
fdbookstore = Bookstore("Fernanda's Books")

#add authors
poe = Author('Edgar Allen Poe', 'UK')
joyce = Author('James Joyce', 'IR')
borges = Author('Jorge Luis Borges', 'AR')


#create books
raven = Book("The Raven", author=poe)
valdemar = Book("Mr. Valdemar", author=poe)
ulysses = Book("Ulysses", author=joyce)
ficciones = Book("ficciones", author=borges)

#add books to store
fdbookstore.add_book(raven)
fdbookstore.add_book(valdemar)
fdbookstore.add_book(ulysses)
fdbookstore.add_book(ficciones)

#initialize
print(fdbookstore.name)
print(fdbookstore.get_books)
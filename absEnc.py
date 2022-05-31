from art import *


class Library:
    def __init__(self, books):
        self.listOfBook = books

    def displayAvailableBook(self):
        for book in self.listOfBook:
            print(book)

    def lendbook(self, requestedBook):
        if requestedBook in self.listOfBook:
            self.listOfBook.remove(requestedBook)
            print('you have taken a book named: ', requestedBook)
        else:
            print('no book available in the list with this name.')

    def addbook(self, returnedBook):
        self.listOfBook.append(returnedBook)
        print('you have returned a book :', returnedBook)


class Customer:
    def requestBook(self):
        print('which book do you want: ')
        requestedBook = input("> ")
        return requestedBook

    def returnBook(self):
        print('enter the name of the book you want to return')
        returndbook = input("> ")
        return returndbook


library = Library(['think and grow rich', 'who will cry when you die', 'one more day'])
customer = Customer()

Art = text2art("Library")
print(Art)
while True:
    print()
    print('input desire number to do specific tasks: ')
    print('input 1 to display available books: ')
    print('input 2 to return a book: ')
    print('input 3 to lend a book: ')
    print('input 4 to quit: ')
    userChoice = int(input('> '))
    if userChoice == 1:
        library.displayAvailableBook()
    elif userChoice == 2:
        retutnbook = customer.returnBook()
        library.addbook(retutnbook)
    elif userChoice == 3:
        requestedBook = customer.requestBook()
        library.lendbook(requestedBook)
    else:
        quit()

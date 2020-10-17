class Library :

    def __init__(self, books) :
        print('books111', books)
        self.books = books
    

    def DisplayAvailableBooks(self) :
        print('Books present in library are: \n')
        for book in self.books:
            print('*', book)

    def BorrowBooks (self, name) :
        if name in self.books:
            print(f'Book {name} is available, will be given and please take care of it and return on time')
            self.books.remove(name)
            return True
        else:
            print('Sorry !, as of now  book is not available')
            return  False
    
    def ReturnBooks (self, name) :
        self.books.append(name)
        print('Thanks for returning it')

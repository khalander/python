from Library import Library
from Student import Student

if __name__ == '__main__' :
    books = ['Python', 'C++', 'Java', 'PHP']
    library = Library(books)
    student = Student()

    while (True) :
        welcome = ''' *********** Central library ***********
            1) List of Books
            2) Request a Book
            3) Return a Book
            4) Exit the Library
        '''
        print(welcome)

        a = int(input('Enter option\n'))

        if (a == 1) :
            library.DisplayAvailableBooks()
        elif a == 2:
            book = student.requestBook()
            library.BorrowBooks(book)
        elif a == 3:
            book = student.returnBook()
            library.ReturnBooks(book)
        elif a == 4:
            exit()
        else:   
            print('Invalid')




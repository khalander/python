class Student :

    def requestBook (self):
        self.book = input('Please enter the book which you want to borrow\n')
        return self.book
    
    def returnBook (self) :
        self.book = input('Please the book which you want to return\n')
        return self.book
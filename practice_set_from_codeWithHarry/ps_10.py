print('--------------PS 1: class to store employee information------------------ \n')

class Programmer :
    company = 'Microsoft'

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"name:{self.name} is working on project: {self.product} in company: {self.company}")


harry = Programmer('Harry', 'gmeet')
alka = Programmer('Alka', 'gmail')

harry.getInfo()
alka.getInfo()

print('--------------PS 2: class to store employee information------------------ \n')

class Calculator :

    def __init__(self, number) :
        self.number = number

    def squareRoot (self):
        value = self.number * 2
        return 'Square root of given number: ' + str(value)

    def cube (self) :
        value = self.number * 3
        return 'Cube of given number: ' + str(value)


calsi = Calculator(2)
print(calsi.squareRoot())
print(calsi.cube())

print('--------------PS 3: Mdofiy class attribute, Will it ? and static method------------------ \n')

class Sample:
    sample_a = 'Mufeez'

    @staticmethod
    def greet() :
        print('***************** Welcome to python world *********************')


rabia = Sample()
rabia.sample_a = 'Rabia'

print(rabia.sample_a)
print(Sample.sample_a)
print(rabia.greet())

print('--------------PS 4: Train book class------------------ \n')

class Train:

    def __init__(self, name, fare, seats):
        self.train = name
        self.fare = fare
        self.seats = seats

    
    def getTrainStatus(self):
        print(f"Status of train: {self.train} is: {self.seats} ")

    def getFare(self):
        print(f'Fare of the train: {self.train} is : {self.fare}')

    def bookTicket(self, number):
        if (self.seats > 0):
            print(f"Total number  of Seats : {number} is booked for train: {self.train}")
            self.seats = self.seats - number        
        else:
            print(f'No seats available for train: {self.train}')
    
    def cancelTicket(self, number) :
        print(f"Number of  ticket cancelled: {number} for train is: {self.train}")
        self.seats = self.seats + number   


bellary = Train('bellary', 300, 5)

print(bellary.getTrainStatus())
print(bellary.getFare())
print(bellary.bookTicket(5))
print(bellary.cancelTicket(5))
print(bellary.bookTicket(5))
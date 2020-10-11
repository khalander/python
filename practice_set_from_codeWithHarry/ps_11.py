
print('--------------PS 1: Vector class (Inheritence example)------------------ \n')

# class C2dVec:

#     def __init__(self, i, j):
#         self.iCap = i
#         self.jCap = j

#     def __str__(self):
#         return f"{self.iCap}i + {self.jCap}j"

# class C3Vedc(C2dVec) :

#     def __init__(self, i, j, k) :
#         super().__init__(i, j)
#         self.kCap = k
    
#     def __str__(self):
#         return f"{self.iCap}i + {self.jCap}j + {self.kCap}k"


# v2d = C2dVec(1, 3)
# v3d = C3Vedc(2, 3, 4)

# print(v2d)
# print(v3d)

print('--------------PS 1: Animal (Multi level example)------------------ \n')

# class Animal :
#     eat = "All animal will eat"


# class Pets(Animal) :
#     motherName = 'Created from animal'

# class Dog(Pets) :

#     @staticmethod
#     def bark() :
#         print('Bow bow')

# dog = Dog()

# print(dog.bark())
# print(dog.motherName)
# print(dog.eat)

print('--------------PS 1: setter and getter example------------------ \n')

class Employee:
    salary = 1000
    increment = 1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary * self.increment
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, sai):
        self.increment = sai/self.salary


e = Employee()
print(e.salaryAfterIncrement)
print(e.increment)

e.salaryAfterIncrement = 2000
print(e.increment)
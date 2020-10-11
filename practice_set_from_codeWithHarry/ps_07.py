print('--------------PS 1: print the table of given  number------------------- \n')
number = int(input('Enter number to print its table: '))

for i in range(1, 11):
    mul = number*i
    print(f"{number} * {i} = {mul}")

print('--------------PS 2:Greet all the persons starting with m------------------- \n')

names = ['mufeez', 'fatima', 'rabia', 'muhammed']

for name in names:
    if name.startswith('m'):
        print('Hello', name)

print('--------------PS 3: print the table of given  number------------------- \n')
number = int(input('Enter the number to print its table\n'))
i = 1
while i < 11 :
    print(f"{number}*{i}={number*i}")
    i = i + 1


print('--------------PS 4: Find is number is prime or not------------------- \n')

num = int(input('Enter number to find is it prime or not'))

prime = True

for i in range(2, num):
    if (num%i == 0):
        prime = False
        break

print(f'Given number {num} is prime: {prime}',)


print('--------------PS 5: Find sum of N natural number------------------- \n')

number = int(input('Enter number to find sum of its natural number '))

total = 0

while (number >= 0) :
    total =  total + number
    number = number - 1

print('Sum of given number is ', total)

print('--------------PS 6: Find factorial of given  number------------------- \n')

number = int(input('Enter a number to find factorial '))

factorial = 1
for i in range(1, number+1):
    factorial = factorial * i

print(f'factorial of given number {number} =>', factorial)

print('--------------PS 7: Find the patter------------------- \n')

n = 4
for i in range(n):
    print(' ' * (n - i -1), end="")
    print('*' * (2*i+1), end="")
    print(' ' * (n-i-1) )

print('--------------PS 8: Find the patter------------------- \n')

n = 4
for i in range(n):
    print('*' * (i+1))

print('--------------PS 9: Find the patter------------------- \n')
 # @todo
n = 3
for i in range(n):
    print('*' * n)

print('--------------PS 10: print the table in reverse manner------------------- \n')

number = int(input('Enter number to print its table: '))

for i in range(10, 0, -1):
    mul = number*i
    print(f"{number} * {i} = {mul}")
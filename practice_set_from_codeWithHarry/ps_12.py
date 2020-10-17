
print('--------------PS 1: Try example------------------ \n')

def readFile (fileName):
    try :
        with open(fileName, 'r') as f :
            print(f.read())
    except FileNotFoundError :
        print (f'file {fileName} is not found')

readFile('a.txt')
readFile('b.txt')
readFile('c.txt')

print('--------------PS 2: Print specified index value------------------ \n')

l = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 11, 21, 13]

for index, item in enumerate(l) :
    if (index == 2 or index == 4 or index == 6) :
        print(f'The index {index+1} element is {item}') 

print('--------------PS 3: list comprehension------------------ \n')

num = int(input('Enter the number to print its table \n'))

for i in range(1, 11) :
    print(f'{num}*{i}={num*i}')

table = [f'{num}*{i}={num*i}' for i in range(1, 11)]
print(table)

with open('table.txt', 'w') as f:
    f.write(str(table))



print('--------------PS 4: Infinite loop handled------------------ \n')
a = int(input('Enter a value: '))
b = int(input('Enter b value: '))

try :
    print(a/b)
except :
    print("Infinite")

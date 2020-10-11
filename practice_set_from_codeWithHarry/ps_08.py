print('--------------PS 1: find the greatest of 3 number using function------------------- \n')


def greatesOf3Number(n1, n2, n3):
    if (n1>n2):
        if (n1>n3):
            return n1
        else :
            return n3
    else :
        if (n2>n3) :
            return n2
        else:
            return n3


a = greatesOf3Number(31,2,4)
print('Greates of 3 numvvers', a)

print('--------------PS 2: convert to fahrenheit to celsius ------------------- \n')

def convertFahrenheitToCelsius(cel):
    return (cel * (9/5)) + 32

c = 0
f = convertFahrenheitToCelsius(c)
print('Converted value of given celsius:', str(f) )

print('--------------PS 3: How to stop print new line ------------------- \n')

print('How are ', end='')
print('you')

print('--------------PS 4: Recursive function to calculate the sum of natural n number ------------------- \n')

def calSum(n):
    if (n == 0):
        return False
    else:
        return n + calSum(n-1)

print(calSum(10))

print('--------------PS 5: Recursive function to print patter ------------------- \n')
def printPatter(n):
    if (n ==0):
        return False
    else:
        print('*' * n)
        return printPatter(n -1)

printPatter(3)

print('--------------PS 6: convert inces to CM ------------------- \n')

def incesToCM(n):
    return n*2.54

print(incesToCM(14))

print('--------------PS 7: Remove given word and strip the string ------------------- \n')


def removeGivenWordAndStripIt(string, word):
    string = string.replace(word, '')
    return string.strip()

string = 'Python is programing language , its  very easy to learn'
word = 'to learn'

print(removeGivenWordAndStripIt(string, word))

print('--------------PS 8:Function to print table of given number ------------------- \n')
def printTableOfGivenNumber(n):
    for i in range(1,11):
        print(f"{n}*{i}={n*i}")
    
    print('---------------------------')


printTableOfGivenNumber(2)
printTableOfGivenNumber(3)
printTableOfGivenNumber(4)
printTableOfGivenNumber(5)
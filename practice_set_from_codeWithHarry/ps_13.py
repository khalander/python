from functools import reduce
print('--------------PS 1: Format example------------------ \n')

name = input('Please enter the name\n')
phone = input('Please enter the phone \n')
marks = input('Please enter the marks \n')

template = " {} has score {} and his phone number is {}";

output = template.format(name, marks, phone)

print(output)

print('--------------PS 2: Print table in vertical format using list comprehension------------------ \n')
num = int(input('Please enter the number to print its table \n'))
table = [ f'{num}*{i}={num*i}' for i in range(1, 11)]
formated = '\n'.join(table)
print(formated)

print('--------------PS 3: Filter example------------------ \n')

lt = [3, 4, 5,6, 7,10 ,15, 20, 23, 25, 25]

DBy5 = filter(lambda a: a % 5 == 0, lt)
print(list(DBy5))

print('--------------PS 4: Reduce example------------------ \n')

lt = [300, 4, 5,6, 7,10 ,15, 20, 23, 25, 25]

mx = reduce(max, lt)
print((mx))


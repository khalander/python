print('--------------PS 1: Store the fruit names in List------------------- \n')

f1 = input('Enter first fruit ')
f2 = input('Enter second fruit ')
f3 = input('Enter third fruit ')
f4 = input('Enter fourth fruit ')


fruits = [f1, f2, f3, f4]

print('Your faviriots fruits', fruits)

print('--------------PS 2: sort the marks entered by users------------------- \n')

first = int(input('Enter first number '))
second = int(input('Enter second number '))
third = int(input('Enter third number '))
fourth = int(input('Enter four number '))
fifth = int(input('Enter fifth number '))
sixth = int(input('Enter sixth number '))


a = [first, second, third, fourth, fifth, sixth]
a.sort()
print(a)

print('--------------PS 3: Check is tuple updated------------------- \n')
t = (4, 5, 6)
t[0] = 12
print(t)

print('--------------PS 4: Sum the array elements------------------- \n')

a = [23, 4, 5, 6]
m1 = a[0] + a[1] + a[2] + a[3]
print('first approach: ', m1)
print('second approach: ', sum(a))

print('--------------PS 5: Count number of zero in array------------------- \n')
a = [3, 4, 0, 3,0 ,5, 0]
print('Number of zero are: ', a.count(0))
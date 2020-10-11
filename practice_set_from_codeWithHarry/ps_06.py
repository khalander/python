print('--------------PS 1: Find greatest of 4 numbers------------------- \n')

num1 = int(input('Enter first number\n'))
num2 = int(input('Enter second number\n'))
num3 = int(input('Enter third number\n'))
num4 = int(input('Enter fourth number\n'))

if (num1 > num4):
    a = num1
else:
    a = num4

if(num2>num3) :
    b = num2
else:
    b = num3

if (a > b) :
    print('Greatest of 4 number is: ', a)
else :
    print('Greatest of 4 number is:', b)


print('--------------PS 2: find is student is pass or fail------------------- \n')


sub1 = int(input('Enter subject 1 marks \n'))
sub2 = int(input('Enter subject 2 marks \n'))
sub3 = int(input('Enter subject 3 marks \n'))

if (sub1 < 33 or sub2 < 33 or sub3 < 33) :
    print('you failed becouse you scored one of subject less then 33')
elif ((sub1+sub2+sub3)/3 < 40):
    print('you failed because avg is less then 40 %')
else:
    print('Congratutions you passed.. you did it')


print('--------------PS 3: Find is text contains spam words------------------- \n')

text = input('Please enter text\n')

if ('make a lot of money' in text):
    print('text is spam')
elif ('buy now' in text):
    print('Text is spam')
elif('subscribe this' in text):
    print('text is  spam')
else:
    print('Text is not spam')


print('--------------PS 4: Find is text contains less then 10 charaters------------------- \n')

text = input('Enter name ')

if (len(text) > 10) :
    print('Valid text')
else:
    print('Less then 10 words')

print('--------------PS 5: Find is user present------------------- \n')

names = ['mufeez', 'rabia', 'fatima', 'kaneez']

text = input('Please enter name ')

if (text in names) :
    print('Name present')
else:
    print('Name not present, hou can use it')

print('--------------PS 6: Find the grade of the student------------------- \n')

marks = int(input('Please enter your marks\n'))

if (marks >= 90) :
    print('Excellend')
elif(marks >= 80) :
    print('A grade')
elif (marks >= 70):
    print('B grade')
elif (marks >= 60):
    print('C grade')
elif (marks >= 50):
    print('Failed')

print('--------------PS 7: Check post contain harry or not------------------- \n')


post = 'testing for post python examples for praticing set harry'

if ('harry' in post):
    print('Exists')
else:
    print('Doesnt exists')


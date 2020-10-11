print('--------------PS 1: Hindi to English dictionary ------------------- \n')

hindiToEng = {
    'naam': 'Name',
    'ladka': 'Boy',
    'ladki': 'Girl',
    'Walidain' : 'parents'
}

# print('Option are: 1) Naam, 2) Ladka, 3) Ladki, 4) Walidain\n')
print('options are', hindiToEng.keys())
word = input('Please enter hindi words\n')

print(f"English translation of your word: {word} =>", hindiToEng.get(word))

print('--------------PS 2: Print unique numbers from user: hint:use set------------------- \n')


first = int(input('Enter first number '))
second = int(input('Enter second number '))
third = int(input('Enter third number '))
fourth = int(input('Enter four number '))
fifth = int(input('Enter fifth number '))
sixth = int(input('Enter sixth number '))
seven = int(input('Enter seven number '))
eight = int(input('Enter eight number '))


# a = {first, second, third, fourth, fifth, sixth, seven, eight}

# print(a)

print('--------------PS 3: can we have set with differnt data type of same value------------------- \n')

a = {18, '18', 18.1}

print(a)

print('--------------PS 4: what is output of this set------------------- \n')

a = set()
a.add(20)
a.add('20')
a.add(20.0)
print(len(a))

print('--------------PS 5: what is type of set------------------- \n')
s = {}
print('Type of set is:', type(s))

print('--------------PS 6: what is type of set------------------- \n')

favorites = {}

a = input('Mufeez, please enter your favorite fruits \n')
b = input('Rabia, Please enter your favorite fruits \n')
c = input('Fatima, Please enter your favorite fruits \n')
d = input('Kaneez, Please enter your favorite fruits \n')

favorites['mufeez'] = a
favorites['rabia'] = b
favorites['fatima'] = c
favorites['kaneez'] = d

print(favorites)
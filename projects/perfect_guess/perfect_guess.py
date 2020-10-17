import random

randomNumber = random.randint(1, 100)

userGuess = None
guesses = 0
#print('randomNumber', randomNumber)
while (userGuess != randomNumber):
    userGuess = int(input('Please enter your guess\n'))
    if (userGuess == randomNumber):
        print('Your guess is correct')
    else :
        if (randomNumber > userGuess):
            print('Hint: Guess higher number\n')
        else:
            print('Hint: Guess lower number\n')
    guesses = guesses + 1

print(f'You guess it at times: {guesses}')

with open('perfect_guess.txt') as f:
    t = f.read()
    if t == '':
        with open('perfect_guess.txt', 'w') as f:
            f.write(str(guesses))
    else:
        if(guesses < int(t)) :
            with open('perfect_guess.txt', 'w') as f:
                f.write(str(guesses))


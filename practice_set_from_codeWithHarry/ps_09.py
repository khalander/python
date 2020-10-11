import os
print('--------------PS 1: Check is given words exists in file or not------------------ \n')

f = open('poem.txt')
t = f.read()
if ('twinkle' in t):
    print('Word exits')
else:
    print('Word not exits')


f.close()

print('--------------PS 2: Update the high score to file------------------ \n')

def game():
    return 455

def writeHighScoreToFile(newScore):
    with open('highscore.txt', 'w') as f:    
        f.write(str(newScore))

newScore = game()
with open('highscore.txt') as f:
    highscore = f.read()
    print('highscore', highscore, highscore == '')
   
if highscore == '':
    writeHighScoreToFile(newScore)

elif int(highscore) < newScore:
    writeHighScoreToFile(newScore)

print('--------------PS 3: Write tables to file------------------ \n')
os.mkdir('tables')
for i in range(2, 21) :
    with open(f"tables/multiplication_table_of_{i}.txt", "w+") as f:
        for j in range(1, 11):
            f.write(f"{i}*{j}={i*j}")
            if j!=10:
                f.write('\n')

print('--------------PS 4: Program to replacw given word in file----------------- \n')

with open('poem.txt') as f:
    t = f.read()
    print(t)
    if ('donkey' in t):
        content = t.replace('donkey', 'XXXXXX')
        with open('poem.txt', 'w') as f:
            f.write(content)
    
f.close()

print('--------------PS 4: Program to censored---------------- \n')

censored = ['donkey', 'monkey', 'kill']

with open('poem.txt') as f:
    t = f.read()

    for word in censored :
        t = t.replace(word, 'XXXXXX')    
        with open('poem.txt', 'w') as f:
            f.write(t)

print('--------------PS 5: Check is log contains python word---------------- \n')
with open('log.txt') as f:
    t =  f.read()
    if ('python' in t.lower()):
        print('Text exists')
    else:
        print('Text doesnt exists')

print('--------------PS 6: Check is log contains python word and print line number---------------- \n')
content = True
exits = False
i = 1
with open('log.txt') as f:
    while (content) :
        content = f.readline()
        if ('python' in content.lower()):
            exits = True
            break
        else:
            i = i + 1

if (exits) :
    print('exits at', i)
else :
    print('Doesnt exits')

print('--------------PS 7: Copy file---------------- \n')

with open('log.txt') as f:
    t = f.read()

with open('copy.txt', 'w') as f:
    f.write(t)

print('--------------PS 8: Copy file---------------- \n')

with open('log.txt') as f:
    f1 = f.read()

with open('copy.txt') as f:
    f2 = f.read()

if f1 == f2:
    print('file are same')
else:
    print('files are not same')

print('--------------PS 9: delete content of file---------------- \n')

with open('copy.txt', 'w') as f:
    f.write('')

print('--------------PS 10: Rename file---------------- \n')

with open('copy.txt') as f:
    content = f.read()

with open('rename.txt', 'w') as f:
    f.write(content)

os.remove('copy.txt')
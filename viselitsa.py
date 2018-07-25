#Игра "Виселица"
import random
words = ['one', 'two', 'three', 'old', 'men', 'women', 'letter', 'paper', 'elephant', 'telephone', 'rush', 'power', 'calculator', 'pen', 'notebook', 'laptop', 'science']
a = random.randint(0, len(words))
computer = words[a]
right_word = []
win = False
health = 10
for i in range(len(computer)):
    right_word.append('_')
while win == False and health > 0 and health <=10:
    men = input("Your word or letter ")
    if men == computer:
        win = True
    elif len(men) != 1 and men != computer:
        print('Enter one letter or right word')
        health -= 1
    else:
        if men not in computer:
            health -= 1
            print("You are loser")
        else:
            print("You are right")
            for i in range(len(computer)):
                if men == computer[i]:
                    right_word[i] = computer[i]
            if str(right_word) == computer:
                win = True
    print(right_word)

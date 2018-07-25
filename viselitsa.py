#Игра "Виселица"
import random
words = ['one', 'two', 'three', 'old', 'men', 'women', 'letter', 'paper', 'elephant', 'telephone', 'rush', 'power', 'calculator', 'pen', 'notebook', 'laptop', 'science']
a = random.randint(0, len(words))
computer = words[a]
win = False
life = -1

def compare(men, computer):
    if men == computer:
        win = True
        print("Win!")
    else:
        if men in computer:
            print("Right!")
            win = False
        if men not in computer:
            print("Wrong!")
            win = False
    return win

while win == False and life < 10:
    life += 1
    men = input("Your word or letter ")
    compare(men, computer)

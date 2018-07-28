#Крестики-нолики
import random

field = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
user, computer= 'o', 'x'
win = False

def enter_user(field):
    try:
        a_user, b_user = int(input('Enter row\n')), int(input('Enter column\n'))
        if a_user > 2 or b_user > 2:
            print('Enter less value')
            a_user, b_user = int(input('Enter row\n')), int(input('Enter column\n'))
    except ValueError:
        print('You haven`t entered some value')
        a_user, b_user = int(input('Enter row\n')), int(input('Enter column\n'))
    if field[a_user][b_user] not in 'xo':
        field[a_user][b_user] = user
    test(win)
    return field

def enter_computer(field):
    a_computer, b_computer = random.randint(0, 2), random.randint(0, 2) 
    while field[a_computer][b_computer] in 'xo':
        a_computer, b_computer = random.randint(0, 2), random.randint(0, 2) 
    field[a_computer][b_computer] = computer
    test(win)
    return field

def test(win):
    #главная диагональ
    if field[0][0] == field[1][1] and field[0][0] == field[2][2]:
        if field [0][0] == 'o':
            win = True
            print('You are winner')
            exit()
        if field [0][0] == 'x':
            win = True
            print('You are loser! The computer is winner')
            exit()
    #побочная диагональ
    if field[0][2] == field[1][1] and field[0][2] == field[2][0]:
        if field [0][2] == 'o':
            win = True
            print('You are winner')
            exit() 
        if field [0][2] == 'x':
            win = True
            print('You are loser! The computer is winner')
            exit()
    #строка1
    if field[0][0] == field[0][1] and field[0][0] == field[0][2]:
        if field [0][0] == 'o':
            win = True
            print('You are winner')
            exit()
        if field [0][0] == 'x':
            win = True
            print('You are loser! The computer is winner')
            exit()
    #строка2
    if field[1][0] == field[1][1] and field[1][0] == field[1][2]:
        if field [1][0] == 'o':
            win = True
            print('You are winner')
            exit()
        if field [1][0] == 'x':
            win = True
            print('You are loser! The computer is winner')
            exit()
    #строка3
    if field[2][0] == field[2][1] and field[2][0] == field[2][2]:
        if field [2][0] == 'o':
            win = True
            print('You are winner')
            exit()
        if field [2][0] == 'x':
            win = True
            print('You are loser! The computer is winner')
            exit()
    #столбец1
    if field[0][0] == field[1][0] and field[0][0] == field[2][0]:
        if field [0][0] == 'o':
            win = True
            print('You are winner')
            exit()
        if field [0][0] == 'x':
            win = True
            print('You are loser! The computer is winner')
            exit()
    #столбец2
    if field[0][1] == field[1][1] and field[0][1] == field[2][1]:
        if field [0][1] == 'o':
            win = True
            print('You are winner')
            exit()
        if field [0][1] == 'x':
            win = True
            print('You are loser! The computer is winner')
            exit()
    #столбец3
    if field[0][2] == field[1][2] and field[0][2] == field[2][2]:
        if field [0][2] == 'o':
            win = True
            print('You are winner')
            exit()
        if field [0][2] == 'x':
            win = True
            print('You are loser! The computer is winner')
            exit()
    else:
        win = False
    return win
print("\n".join(str(x) for x in field))
for i in range(3):
    while ' ' in field[i]:
        enter_user(field)
        print("\n".join(str(x) for x in field))
        print('\n')
        enter_computer(field)
        print("\n".join(str(x) for x in field))
    
print("Game over!")

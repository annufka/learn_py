#Крестики-нолики
import random
def test(win):
    #главная диагональ
    if field[0][0] == field[1][1] and field[0][0] == field[2][2]:
        if field [0][0] == 'o':
            win = True
            print('You are winner')
        if field [0][0] == 'x':
            win = True
            print('You are loser! The computer is winner')
    #побочная диагональ
    if field[0][2] == field[1][1] and field[0][2] == field[2][0]:
        if field [0][2] == 'o':
            win = True
            print('You are winner')
        if field [0][2] == 'x':
            win = True
            print('You are loser! The computer is winner')
    #строка1
    if field[0][0] == field[0][1] and field[0][0] == field[0][2]:
        if field [0][0] == 'o':
            win = True
            print('You are winner')
        if field [0][0] == 'x':
            win = True
            print('You are loser! The computer is winner')
    #строка2
    if field[1][0] == field[1][1] and field[1][0] == field[1][2]:
        if field [1][0] == 'o':
            win = True
            print('You are winner')
        if field [1][0] == 'x':
            win = True
            print('You are loser! The computer is winner')
    #строка3
    if field[2][0] == field[2][1] and field[2][0] == field[2][2]:
        if field [2][0] == 'o':
            win = True
            print('You are winner')
        if field [2][0] == 'x':
            win = True
            print('You are loser! The computer is winner')
    #столбец1
    if field[0][0] == field[1][0] and field[0][0] == field[2][0]:
        if field [0][0] == 'o':
            win = True
            print('You are winner')
        if field [0][0] == 'x':
            win = True
            print('You are loser! The computer is winner')
    #столбец2
    if field[0][1] == field[1][1] and field[0][1] == field[2][1]:
        if field [0][1] == 'o':
            win = True
            print('You are winner')
        if field [0][1] == 'x':
            win = True
            print('You are loser! The computer is winner')
    #столбец3
    if field[0][2] == field[1][2] and field[0][2] == field[2][2]:
        if field [0][2] == 'o':
            win = True
            print('You are winner')
        if field [0][2] == 'x':
            win = True
            print('You are loser! The computer is winner')
    else:
        win = False
    if win == True:
        print("\n".join(str(x) for x in field))
        quit()
    return win

field = [['','',''],['','',''],['','','']]
empty = ['']
user, computer= 'o', 'x'
win = False

while win == False:
#проверка на наличие пустых полей
    for i in range(3):
        for j in range(3):
            if empty[0] == field[i][j]:
            
                try:
                    a_user, b_user = int(input()), int(input())
                except ValueError:
                    print('Вы не ввели значение')
                    a_user, b_user = int(input()), int(input())
                field[a_user][b_user] = user
                test(win)
                a_computer, b_computer = random.randint(0, 2), random.randint(0, 2) 
                if empty[0] == field[a_computer][b_computer]:
                    field[a_computer][b_computer] = computer
                    test(win)
                else:
                    while empty[0] != field[a_computer][b_computer]:
                        a_computer, b_computer = random.randint(0, 2), random.randint(0, 2)
                        if empty[0] == field[a_computer][b_computer]:
                            field[a_computer][b_computer] = computer
                            test(win)
                
                print("\n".join(str(x) for x in field))
                
print("Game over!")

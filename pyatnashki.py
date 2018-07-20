import random
def test(field):
    my_field = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,'x']]
    if field==my_field:
        game = False
        print('Win!')

def moves(move):
    for a in range(4):
        for b in range(4):
            if field[a][b] == 'x':
                if move == 'w':
                    try:
                        field[a][b], field[a-1][b] = field[a-1][b], field[a][b]
                    except IndexError:
                        print('Cant move up')
                try:
                    if move == 's':
                        field[a][b], field[a+1][b] = field[a+1][b], field[a][b]
                except IndexError:
                        print('Cant move down')
                try:
                    if move == 'a':
                        field[a][b], field[a][b-1] = field[a][b-1], field[a][b]
                except IndexError:
                        print('Cant move right')
                try:
                    if move == 'd':
                        field[a][b], field[a][b+1] = field[a][b+1], field[a][b]
                except IndexError:
                        print('Cant move left')
    
    print("\n".join(str(x) for x in field))

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 'x']
random.shuffle(my_list)
field = [[0] * 4 for i in range(4)]
k = 0
for i in range(4):
    for j in range(4):
        field[i][j] = my_list[k]
        k += 1
print("\n".join(str(x) for x in field))
game = True
s = 0
while game == True:
    s += 1
    moves(move = input())
        

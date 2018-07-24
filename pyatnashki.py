import random
def test(field):
    my_field = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,'x']]
    my_field_other = [[1,5,9,13],[2,6,10,14],[3,7,11,15],[4,8,12,'x']]
    if field==my_field or field==my_field_other:
        game = False
        print('Win!', s)

def moves(move):
    for a in range(4):
        for b in range(4):
            if field[a][b] == 'x':
                if move == 'w':
                    try:
                        if a == 0:
                            raise IndexError('Can`t move up')
                        else:
                            field[a][b], field[a-1][b] = field[a-1][b], field[a][b]
                    except IndexError:
                        print('Can`t move up')
                if move == 's':
                    try:
                        field[a][b], field[a+1][b] = field[a+1][b], field[a][b]
                    except IndexError:
                        print('Can`t move down')
                if move == 'a':
                    try:
                        if b == 0:
                            raise IndexError('Can`t move up')
                        else:
                            field[a][b], field[a][b-1] = field[a][b-1], field[a][b]
                    except IndexError:
                        print('Can`t move right')
                if move == 'd':
                    try:
                        field[a][b], field[a][b+1] = field[a][b+1], field[a][b]
                    except IndexError:
                        print('Can`t move left')
                break
    
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
    try:
        s += 1
        moves(move = input())
    except KeyboardInterrupt:
        print('shutting down')

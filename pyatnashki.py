def move(wasd):
    return(wasd)
import random
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 'x']
random.shuffle(my_list)
field = [[0] * 4 for i in range(4)]
k = 0
for i in range(4):
    for j in range(4):
        field[i][j] = my_list[k]
        k += 1

#Сортировка методом "пузырька" с вводом с клавиатуры
my_list = []
n = 1
for i in range(6):
    a = int(input())
    my_list.append(a)
while n < len(my_list):
    for j in range(1, 6):
        if my_list[j] < my_list[j-1]:
            my_list[j-1], my_list[j] = my_list[j], my_list[j-1]
print(my_list)

#Сортировка методом "пузырька" с random
import random
my_list = []
n = 1
for i in range(6):
    a = random.randint(1, 10)
    my_list.append(a)
while n < len(my_list):
    for j in range(1, 6):
        if my_list[j] < my_list[j-1]:
            my_list[j-1], my_list[j] = my_list[j], my_list[j-1]
print(my_list)

#сортировка выбором
import random
my_list = []
n = 1
for i in range(6):
    a = random.randint(1, 10)
    my_list.append(a)
for k in range(len(my_list) - 1):
        m = k
        i = k + 1
        while i < len(my_list):
            if my_list[i] < my_list[m]:
                m = i
            i += 1
        t = my_list[k]
        my_list[k] = my_list[m]
        my_list[m] = t

#словарь из 5 пар: int -> str
my_dict = {}
for i in range(6):
    my_dict.update({int(input()): input()})
print(my_dict)

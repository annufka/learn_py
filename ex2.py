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

#tuple из 10 любых дробных чисел, найти максимальное и минимальное значение в нем
my_tuple = ()
for i in range(10):
    n = float(input())
    my_tuple += (n, )
min_el = my_tuple[0]
max_el = my_tuple[0]
for j in range(1, len(my_tuple)):
    if my_tuple[j] < min_el:
        min_el = my_tuple[j]
    if my_tuple[j] > max_el:
        max_el = my_tuple[j]
print(min_el, max_el)



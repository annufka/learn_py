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

#лист из 3 слов: ['Earth', 'Russia', 'Moscow'], соеденить все слова в единую строку, чтобы получилось: 'Earth -> Russia -> Moscow'
my_list = ['Earth', 'Russia', 'Moscow']
print(" -> ".join(my_list))

#строку '/bin:/usr/bin:/usr/local/bin' и разбить ее в список по символу ':'
my_str = '/bin:/usr/bin:/usr/local/bin'
new_str = my_str.split(":")
for i in range(len(new_str)):
    print(new_str[i])
    
#все числа от 1 до 100, какие из них делятся на 7, а какие - нет
list_7 = []
other_list = []
for i in range(1, 101):
    if i%7 == 0:
        list_7.append(i)
    else:
        other_list.append(i)
print("Делятся на 7:", list_7, "Не делятся:", other_list)

#матрица любых чисел 3 на 4, сначала вывести все строки, потом все столбцы
import random
matrix = []
for i in range(3):
    matrix.append([])
    for j in range(4):
        a = random.randint(1, 10)
        matrix[i].append(a)
print('строки\n')
for row in range(3):
    print(matrix[row])
print('колонки\n')
for col in range(4):
    print('\n')
    for row in range(len(matrix)):
        print(matrix[row][col], end = ' ')
        
#список любых объектов, в цикле напечатать в консоль: объект и его индекс
my_list = []
n = int(input("Введико количество элементов списка \n"))
for i in range(n):
    a = input()
    my_list.append(a)
for j in range(n):
    print(j, "-й элемент списка - ", my_list[j])

#список с тремя значениями 'to-delete' и нескольми любыми другими, удалить из него все значения 'to-delete'
to_delete = ['pop', 'remove', 'del']
to_delete.pop(0)
to_delete.remove('remove')
del to_delete[0]
print(to_delete)

#пройти по всем числам от 1 до 10 в обратную сторону
for i in range(10, 0, -1):
    print(i)

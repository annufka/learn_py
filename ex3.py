#функция, которая складывает введенные числа
def sum_all(*numbers):
    s = 0
    for i in range(len(numbers)):
        s += numbers[i]
    return(s)

d = sum_all(5,4,10,20,36)
print(d)

#Пользователь вводит число, если оно четное - выбрасываем исключение ValueError, 
#если оно меньше 0 - TypeError, если оно больше 10 - IndexError. Обрабатываем ошибку, 
#говорим пользователю, в чем его ошибка

n = int(input())
try:
    if n <= 10 and n % 2 == 0:
        raise ValueError('ValueError')
except TypeError:
    print('Error')        
    if n < 0: 
        raise TypeError('TypeError')
except TypeError:
    print('Error')
    if n > 10:
        raise IndexError('IndexError')
except TypeError:
    print('Error of types')
except ValueError:
    print('Error of types')
except IndexError:
    print('Error of index')
    
#Создайте список произвольной длины. Пользователь должен ввести индекс объекта, 
#который хочет посмотреть. Если все хорошо - пишите объект в консоль. 
#Если нет - обработайте возмозможные ошибки и скажите ему, что не так
import random
my_list = []
n = random.randint(1, 50)
for i in range(n):
    m = random.randint(1, 1000)
    my_list.append(m)
a = int(input())
try:
    print(my_list[a])
except IndexError:
    print('Не существующий индекс')
    
#Написать функцию, которая принимает на вход два аргумента. Если аргументы 
#больше нуля, возвращаем их сумму. Если оба меньше - разность. 
#Если знаки разные - возвращаем 0
def my_function(a, b):
    s = 0
    if a > 0 and b > 0:
        s = a + b
    if a < 0 and b < 0:
        s = a - b
    print(s)
    return(s)
n = int(input())
c = int(input())
my_function(n, c)

#Написать функцию, которая принимает 3 аргумента - числа, найти среди них два максимальных, вывести в консоль
def function_max(a, b, c):
    min_n = 0
    for i in range(1, 3):
        if a < b and a < c:
            min_n = a
            print(b, c)
        if b < a and b < c:
            min_n = b
            print(a, c)
        if c < a and c < b:
            min_n = c
            print(a, b)
    return(a, b, c)
a = int(input())
b = int(input())
c = int(input())
function_max(a, b, c)

#Написать функцию, которая принимает два аргумента. Первый - список чисел, второй - булевый флаг. 
#Если флаг действителен - возвращаем новый список с нечетными числами из входного списка, если флаг 
#отрицателен - возвращаем новый список с четными числами из входного списка
def funct(*my_list, YesOrNo = False):
    my_list = list(my_list)
    if YesOrNo == True:
        for i in range(len(my_list) -1, -1, -1):
            if my_list[i] % 2 != 0:
                my_list.pop(i)
    else:
        for i in range(len(my_list) -1, -1, -1):
            if my_list[i] % 2 == 0:
                my_list.pop(i)
    print(my_list)
                
funct(1, 6, 2, 50, 2, 7, 1, 3, YesOrNo = True)

#Написать функцию, которая принимает любое количество аргументов чисел. Среди них она находит максимальное 
#и минимальное. И возвращает оба
def funct(*numbers):
    numbers = list(numbers)
    print(min(numbers), max(numbers))

funct(1, 0, 6, 10, 34, 12, 45, 64)

#Написать функцию, которая принимает два аргумента: строка и булевый флаг case по-умолчанию равный True. 
#Если флаг действителен: возвращаем новую строку, где каждый символ входной приведен к верхнему регистру, 
#иначе - к нижнему
def funct(*words, case = True):
    if case == True:
        s = str(words).upper()
        print(s)
    else:
        s = str(words).lower()
        print(s)
        
    return(s)
funct("hello my dear. if you read this text i find my program", case = True)

#Написать функцию, которая принимает любое количество позиционных аргументов - строк и один парматер 
#по-умолчанию glue, который равен ':'. Соединить все строки таким образом, чтобы в результат попали 
#все строки, длинее 3 символов. Для соединения между любых двух строк вставлять glue
def function(*args, glue=':'):
    print(glue.join([x for x in args if len(x) > 3]))

function("kjkd", "fdkhlk", "f", "fdfgfghtr")

'''
Напишите программу, которая принимает на вход список целых чисел и выводит на экран значения, которые повторяются в нём более одного раза.
Для решения задачи может пригодиться метод sort списка.
Формат ввода:
Одна строка с целыми числами, разделёнными пробелом.
Формат вывода:
Строка, содержащая числа, разделённые пробелом. Числа не должны повторяться, порядок вывода может быть произвольным.
Sample Input:
4 8 0 3 4 2 0 3
Sample Output:
0 3 4
'''
s = list(input().split())

s.sort()
m = []
for i in range(1, len(s)):
    if s[i-1] == s[i]:
        if s[i] not in m:
          m.append(s[i])
        
print(" ".join(m))


'''
Вы решили написать преобразователь кода на Python в код на Java. Так как на Java принят стандарт наименования CamelCase, то вы решили научиться преобразовывать имена из underscore в этот формат. 
Для начала напишите программу, которая переводит имена переменных из стиля написания underscore в стиль UpperCamelCase.
Стиль underscore характеризуется тем, что слова в имени пишутся маленькими буквами и разделяются между собой символом подчёркивания "_". Стиль UpperCamelCase означает, что каждое слово пишется с большой буквы и разделителей между словами нет.
Формат ввода:
Одна строка, содержащая имя, записанное в формате underscore.
Формат вывода:
Строка, содержащая пришедшее имя в формате UpperCamelCase.
Sample Input 1:
my_first_class
Sample Output 1:
MyFirstClass
Sample Input 2:
a
Sample Output 2:
A
'''
name_py = input()
name_js = []
name_js.append(name_py[0].upper())
for i in range(1, len(name_py)):
    if name_py[i] == '_':
        pass
    if name_py[i] != '_':
        if name_py[i-1] == '_':
            name_js.append(name_py[i].upper())
        else:
            name_js.append(name_py[i])
print("".join(name_js))


'''
Выведите таблицу размером n×n, заполненную целыми числами от 1 до n2 по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере.
Формат ввода:
Одна строка, содержащая одно целое число n, n>0.
Формат вывода:
Таблица из n строк, значения в строках разделены пробелом.
'''
def zm(n):
    dx, dy = 1, 0
    x, y = 0, 0
    arr = [[None] * n for _ in range(n)]
    for i in range(1, n**2+1):
        arr[x][y] = i
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < n and not arr[nx][ny]:
            x, y = nx, ny
        else:
            dx, dy = -dy, dx
            x, y = x+dx, y+dy
    for x in list(zip(*arr)):
        print(*x)

zm(int(input()))


'''
Напишите программу, которая выводит число в стиле LCD калькулятора.
На вход программе подаётся последовательность цифр, которую нужно вывести на экран в специальном стиле (см. пример).
Размер всех цифр 4 символа в ширину и 7 символов в высоту. Между цифрами в выводе должен быть один пустой столбец. Перед первой цифрой не должно быть пробелов.
Выведенные цифры должны быть обведены рамочкой, в углах которой находится символ x ("икс"), горизонтальная линия создаётся из символа - ("дефис"), а вертикальная -- из символа вертикальной черты: |.
Формат ввода:
Строка произвольной длины (минимум один символ), содержащая последовательность цифр.
Формат вывода:
9 строк, содержащих цифры, записанные в указанном в задании формате.
'''
class Numbers(object):
  def One(self, i, j):
    for a in range(1, 7):
      for b in range(j, j+3):
        lsd[a][b] = ' '
    b += 1
    for a in range(1, 7):
      if a == 1 or a == 4 or a == 7:
        lsd[a][b] = ' '
      else:
        lsd[a][b] = '|'
    return lsd[a][b]


  def Two(self, i, j):
    pass
  def Three(self, i, j):
    pass
  def Four(self, i, j):
    pass
  def Five(self, i, j):
    pass
  def Six(self, i, j):
    pass
  def Seven(self, i, j):
    pass
  def Eight(self, i, j):
    pass
  def Nine(self, i, j):
    pass
  def Zero(self, i, j):
    pass


numbers = input()
n = len(numbers) * 4 + len(numbers) + 1
lsd = [[None] * n for _ in range(9)]
k = 0
for i in range(9):
    for j in range(n):
      if i == 0 or i == 8:
        if (j == 0 or j == n-1) and lsd[i][j] == None:
          lsd[i][j] = 'x'
        if (j != 0 or j != n-1) and lsd[i][j] == None:
          lsd[i][j] = '-'
      if i != 0 or i != 8:
        if (j == 0 or j == n-1) and lsd[i][j] == None:
          lsd[i][j] = '|'
        if (j != 0 or j != n-1) and lsd[i][j] == None:
          if numbers[k] == 0:
            a = Numbers()
            a.Zero(i, j)
          if numbers[k] == 1:
            a = Numbers()
            a.One(i, j)
          if numbers[k] == 2:
            a = Numbers()
            a.Two(i, j)
          if numbers[k] == 3:
            a = Numbers()
            a.Three(i, j)
          if numbers[k] == 4:
            a = Numbers()
            a.Four(i, j)
          if numbers[k] == 5:
            a = Numbers()
            a.Five(i, j)
          if numbers[k] == 6:
            a = Numbers()
            a.Six(i, j)
          if numbers[k] == 7:
            a = Numbers()
            a.Seven(i, j)
          if numbers[k] == 8:
            a = Numbers()
            a.Eight(i, j)
          if numbers[k] == 9:
            a = Numbers()
            a.Nine(i, j)
          '''
          lsd[i][j] = None 
          '''         
       
print("\n".join(str(x) for x in lsd))

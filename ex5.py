'''
*ЗАДАЧА 1:
1. Создать класс корзина, у которого можно выставить разную вместительность для разных объектов.
В объекты класса корзина можно помещать разные объекты;
2. Вам нужно создать класс пакет, в который тоже можно помещать предметы. У него тоже есть вместимость;
3. Создать любой класс, объекты которого можно было бы мощешать в корзину и пакет;
4. Если вместимости недостаточно, сказать, что объект поместить нельзя.
'''
class Basket(object):
    def __init__(self, capacity):
        self.capacity = capacity
    def change_capacity(self, capacity):
        self.capacity = capacity
    def get_capacity(self):
        print('The capacity of this basket is {}'.format(self.capacity))
    def put_smth(self, smth):
        if smth.capacity <= self.capacity:
            print('You put {} in the basket'.format(smth))
        else:
            print('Your {} is to big for this basket'.format(smth))

class Package(Basket):
    def get_capacity(self):
        print('The capacity of this packege is {}'.format(self.capacity))
    def put_smth(self, smth):
        if smth.capacity <= self.capacity:
            print('You put {} in the packege'.format(smth))
        else:
            print('Your {} is to big for this packege'.format(smth))

class Thing(object):
    def __init__(self, capacity):
        self.capacity = capacity

a = int(input('The capacity of basket is '))
b = int(input('The capacity of packege is '))
c = int(input('The capacity of thing is '))
d = int(input('The capacity of thing is '))

i = Basket(a)
i.get_capacity()

j = Package(b)
j.get_capacity()

smth1 = Thing(c)
smth2 = Thing(d)

i.put_smth(smth1)
i.put_smth(smth2)

j.put_smth(smth1)
j.put_smth(smth2)

'''
*ЗАДАЧА 2:
Пользователь вводит список чисел через пробел. если ввел:
1 число, строим квадрат
2 числа, строим прямоугольник
3 числа, треугольник
4 числа, многоугольник

вычисляем периметр и площадь. выводим в консоль.
можно сделать проверки на "возможность" построить данную фигуру с 
такими сторонами.
'''
'''
Пользователь вводит список чисел через пробел. если ввел:
1 число, строим квадрат
2 числа, строим прямоугольник
3 числа, треугольник
4 числа, многоугольник

вычисляем периметр и площадь. выводим в консоль. 
можно сделать проверки на "возмонжость" построить данную фигуру с такими сторонами.
'''
user_input = input('Enter your number or numbers with spase \n').split()

class Figure(object):
    def __init__(self, len_input):
        self.len_input = len_input
    def square_p(self, number):
        self.p = 4 * int(number[0])
        return self.p
    def square_s(self, number):
        self.s = int(number[0]) ** 2
        return self.s
    def rectangle_p(self, number):
        self.p = (int(number[0]) + int(number[1])) * 2
        return self.p
    def rectangle_s(self, number):
        self.s = int(number[0]) * int(number[1])
        return self.s
    def triangle_p(self, number):
        self.p = int(number[0]) + int(number[1]) + int(number[2])
        return self.p
    def triangle_s(self, number):
        p = int(number[0]) + int(number[1]) + int(number[2])
        h = 2/int(number[0]) * (p * (p - int(number[0]))*(p - int(number[1]))*(p - int(number[2]))) ** 0.5
        self.s = int(number[2]) * h
        return self.s
    def polygon_p(self, number):
        self.p = int(number[0]) + int(number[1]) + int(number[2]) + int(number[3])
        return self.p
    def polygon_s(self, number):
        self.s = 'Error, I don`t know what you want'
        return self.s

if len(user_input) < 1 or len(user_input) > 4:
    print('You enter incorrect value!')
else:
    if len(user_input) == 1:
        a = Figure(user_input)
        print('P = {}, S = {}'.format(a.square_p(user_input), a.square_s(user_input)))
    elif len(user_input) == 2:
        a = Figure(user_input)
        print('P = {}, S = {}'.format(a.rectangle_p(user_input), a.rectangle_s(user_input)))
    elif len(user_input) == 3:
        a = Figure(user_input)
        print('P = {}, S = {}'.format(a.triangle_p(user_input), a.triangle_s(user_input)))
    elif len(user_input) == 4:
        a = Figure(user_input)
        print('P = {}, S = {}'.format(a.polygon_p(user_input), a.polygon_s(user_input)))


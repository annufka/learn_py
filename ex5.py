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


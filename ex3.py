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

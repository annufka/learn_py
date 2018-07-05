#вопрос №1
s = 0
right = 0
n = input("Какой язык мы учим?\n")
if n.lower() == "python":
    right += 1
else:
    right = right
s += 1

#вопрос №2
n = input("Тип целых чисел...\n")
if n.lower() == "int":
    right += 1
else:
    right = right
s += 1

#вопрос №3
n = input("Тип чисел с плавающей запятой...\n")
if n.lower() == "float":
    right += 1
else:
    right = right
s += 1

#вопрос №4
n = input("Какой тип имеет 2 значения?\n")
if n.lower() == "bool":
    right += 1
else:
    right = right
s += 1

#вопрос №5
n = input("Значение булевой, соответствующее \'0\'\n")
if n.lower() == "false":
    right += 1
else:
    right = right
s += 1

#вопрос №6
n = input("Значение булевой, соответствующее числу от 1\n")
if n.lower() == "true":
    right += 1
else:
    right = right
s += 1

#вопрос №7
n = input("Особый тип данный\n")
if n.lower() == "none":
    right += 1
else:
    right = right
s += 1

#вопрос №8
n = input("Можно ли сравнивать с None?\n")
if n.lower() == "да":
    right += 1
else:
    right = right
s += 1

#вопрос №9
n = input("Можно ли производить математические операции с None?\n")
if n.lower() == "нет":
    right += 1
else:
    right = right
s += 1

#вопрос №10
n = input("Можно ли делить строку на строку?\n")
if n.lower() == "нет":
    right += 1
else:
    right = right
s += 1

print("Всего ответов {}, из них правильных ответов {}".format(s, right))

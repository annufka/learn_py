#Сортировка методом "пузырька"
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

#

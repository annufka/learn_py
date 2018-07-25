#Угадай число
import random
WIN = False
computer = random.randint(1, 50)
def compare(computer, men):
    if computer == men:
        print("You are winner!")
        WIN = True
    if computer > men:
        print("My number is greater...")
        WIN = False
    if computer < men:
        print("My number is less...")
        WIN = False
    return WIN

while WIN == False:
    men = int(input("Input your number"))
    compare(computer, men)

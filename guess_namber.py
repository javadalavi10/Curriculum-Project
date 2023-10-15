#دربازی حدس عدد پس از برنده شدن تعداد حدس های کابر راچاپ کند

import random

a=0
b=0
computer_number=random.randint(10,40)
print("You have only 10 chances!")

for i in range(10):
    user_number = int(input("Guess what number I am:"))
    b=b+1

    if computer_number == user_number:
        print("you win")
        a+1
        break

    elif computer_number > user_number:
        print("go up""👆")
        computer_number = user_number +1

    elif computer_number < user_number:
        print("go down""👇")
        computer_number = user_number +1

    if a == 0:

      print("user_number")
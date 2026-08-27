# test
import random
num = random.randint(1, 3)
print(num)
while True:
    choice = int(input("Predict the number from 1 to 3: "))
    if choice == num:
        print("You guessed it right!")
        break
    else:
        print("Wrong")

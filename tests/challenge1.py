# test
import random

while True:
    mode = input("Choose a mode: \n1 for guessing \n2 for calculator \n Your choice: ")
    if mode == "1":
        num = random.randint(1, 3)
        while True:
            choice = int(input("Predict the number from 1 to 3: "))
            if choice == num:
                print("You guessed it right!")
                break
            else:
                print("Wrong")
    elif mode == "2":
        while True:
            operation = input("Choose an operation: +, -, *, / or exit to exit: ")
            if operation == 'exit':
                break
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            if operation == '+':
                print(f"The result is: {num1 + num2}")
            elif operation == '-':
                print(f"The result is: {num1 - num2}")
            elif operation == '*':
                print(f"The result is: {num1 * num2}")
            elif operation == '/':
                if num2 != 0:
                    print(f"The result is: {num1 / num2}")
                else:
                    print("Cannot divide by zero.")
            else:
                print("Invalid operation. Please try again.")

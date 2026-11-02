from random import randint

def first_task():
    try:
        with open("name.txt", "r") as file:
            name = file.read().strip()
            print(f"Hello, {name}! Welcome back!")
    except FileNotFoundError:
        name = input("What is your name? ")
        with open("name.txt", "w") as file:
            file.write(name)
        print(f"Hello, {name}! Nice to meet you!")


def second_task():
    try:
        with open("runs.txt", "r") as file:
            runs = int(file.read().strip())
            runs += 1
    except FileNotFoundError:
        runs = 1

    with open("runs.txt", "w") as file:
        file.write(str(runs))

    print(f"Number of times the program has run: {runs}")


def third_task():
    with open("numb.txt", "w") as file:
        for i in range(100):
            file.write(f"{randint(1, 70)}\n")

    print("100 random numbers generated!")


def fourth_task():
    numbers = []

    with open("numb.txt", "r") as file:
        for lin in file:
            numbers.append(int(lin.strip()))

    deleted = 0
    index = 0

    while index < len(numbers):
        search_value = numbers[index]
        i = index + 1

        while i < len(numbers):
            if search_value == numbers[i]:
                numbers.pop(i)
                deleted += 1
            else:
                i += 1

        index += 1

    with open("numb.txt", "w") as file:
        for number in numbers:
            file.write(str(number) + "\n")

    print("Numbers deleted:", deleted)
    return deleted


def fifth_task(deleted):
    with open("numb.txt", "a") as file:
        for i in range(deleted):
            file.write(str(randint(71, 150)) + "\n")

    print("Numbers added:", deleted)


def sixth_task():
    numbers = []

    with open("numb.txt", "r") as file:
        for line in file:
            numbers.append(int(line.strip()))

    n = len(numbers)

    for i in range(n - 1):
        swapped = False

        for j in range(n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True

        if not swapped:
            break

    with open("numb.txt", "w") as file:
        for number in numbers:
            file.write(str(number) + "\n")

    print("Numbers sorted!")


def seventh_task():
    odd_numbers = []

    with open("numb.txt", "r") as file:
        for line in file:
            number = int(line.strip())

            if number % 2 != 0:
                odd_numbers.append(number)

    with open("odd.txt", "w") as file:
        for number in odd_numbers:
            file.write(str(number) + "\n")

    print("Odd numbers found:", len(odd_numbers))


#first_task()
#second_task()
#third_task()
#deleted = fourth_task()
#fifth_task(deleted)
#sixth_task()
seventh_task()
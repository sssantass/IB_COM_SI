n = int(input("Number of integers:  "))
integers = []
sum_all = 0
sum_even = 0
sum_odd = 0
for i in range(n):
    num = int(input(f"Number {i}:  "))
    integers.append(num)
for i in integers:
    if i%2 ==  0:
        sum_even += i
    else:
        sum_odd += i
    sum_all += i
print(integers)
print(f"All: {sum_all}")
print(f"Even: {sum_even}")
print(f"Odd: {sum_odd}")
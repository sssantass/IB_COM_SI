list = [9,1,5,8,7,2,1,5,5,6,8
        ,15,3,9,19,18,88,10,1,
        100,4,8]
target = int(input("Enter target: "))
data = []
for value in list:
    data.append(value)
found = False
for value in data:
    if value == target:
        found = True
        break
if found:
    print("found")
else:
    print("not found")
list = [9,1,5,8,7,2,1,5,5,6,8
        ,15,3,9,19,18,88,10,1,
        100,4,8]
for i in range (len(list)-1):
    min = i
    for j in range(i+1, len(list)):
        if list[j] < list[min]:
            min = j
    list[i], list[min] = list[min], list[i]
    print(list)
print(f"Final: {list}")
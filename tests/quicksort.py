data = [7, 2, 1, 8, 6, 5, 3, 4,7,1,5,3,8,56,9,1,6,5,90,1,2,45,7,32567,4,242,1,3,57,767,5,4,2,4,5,5,3,37,987,66,7,7,6,66,6,6]

def quicksort(data):
    if len(data) <= 1:
        return data
    pivot = data[0]
    left = []
    right = []

    for i in range(1, len(data)):
        if data[i] <= pivot:
            left.append(data[i])
        elif data[i] > pivot:
            right.append(data[i])
    return quicksort(left) + [pivot] + quicksort(right)
print(quicksort(data))
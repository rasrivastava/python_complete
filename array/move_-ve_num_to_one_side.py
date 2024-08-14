arr = [5, -1, 10, -6, -5, 8, 4, -9]

position = 0

for index in range(len(arr)):
    if arr[index] < 0:
        arr[position], arr[index] = arr[index], arr[position]
        position = position + 1

for num in range(len(arr)):
    print(arr[num], end=" ")

print()

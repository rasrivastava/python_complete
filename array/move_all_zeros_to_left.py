arr = [0, 1, 0, 3, 12, 0]
left = 0

for index in range(len(arr)):
    if arr[index] == 0:
        arr[left], arr[index] = arr[index], arr[left]
        left += 1

for index in range(len(arr)):
    print(arr[index], end=" ")
print()

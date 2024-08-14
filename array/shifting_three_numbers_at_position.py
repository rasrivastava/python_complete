arr = [1, 0, 2, 2, 1, 0, 1, 0]

left = 0
right = len(arr) - 1
index = 0

while (index <= right):
    if arr[index] == 0:
        arr[left], arr[index] = arr[index], arr[left]
        left = left + 1
        index = index + 1
    elif arr[index] == 2:
        arr[right], arr[index] = arr[index], arr[right]
        right = right - 1
    else:
        index = index + 1

for index in range(len(arr)):
    print(arr[index], end=" ")
print()

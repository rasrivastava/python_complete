arr = [[5, 3, 5], [6, 1, 6], [8, 9, 2]]

temp = -1

for i in range(len(arr[0])):
    for j in range(len(arr)):
        if arr[i][j] > temp:
            temp = arr[i][j]

print(temp)

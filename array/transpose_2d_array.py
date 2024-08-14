arr_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

print("before rotation")
for i in arr_2:
    print(i)

"""
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
[10, 11, 12]
"""

transpose = []

for i in range(len(arr_2[0])):
    new_row = []
    for j in range(len(arr_2)):
        new_row.append(arr_2[j][i])
    transpose.append(new_row)

for i in transpose:
    print(i)

"""
[1, 4, 7, 10]
[2, 5, 8, 11]
[3, 6, 9, 12]
"""
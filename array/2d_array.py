arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

"""
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
"""
for row in arr:
    print(row)

"""
1 2 3 4 5 6 7 8 9
"""
for row in arr:
    for element in row:
        print(element, end=" ")
print()

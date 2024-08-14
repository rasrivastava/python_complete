########################
my_set = [1]

# remaining[:i] + remaining[i+1:]

print(my_set[:0])
print(my_set[1+0:])
print(my_set[:0] + my_set[1+0:])
print("-------------------")
######################################

my_set = [1, 2, 3, 4, 5, 6, 7, 8]

# [1, 2, 3, 4, 5, 6, 7, 8]
print(my_set[:])  # Prints the entire list

# [2, 3, 4, 5, 6, 7, 8]
print(my_set[1:]) # Prints the list starting from index 1 to the end

# [1, 2, 3]
print(my_set[:3]) # Prints the list from the beginning up to but not including index 3

# [2, 3]
print(my_set[1:3]) # print the list from 1 but not include 3

print(my_set[::2]) # [1, 3, 5, 7]
print(my_set[::3]) # [1, 4, 7]


s1 = "RAHUL"

print(s1[1:]) # AHUL

print(s1[1:4]) # AHU

print(s1[1:-1]) # AHU

print(s1[::1]) # RAHUL
print(s1[::2]) # RHL
print(s1[::-1]) # LUHAR --> string reverse

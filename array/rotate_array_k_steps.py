nums = [1, 2, 3, 4, 5]
size = len(nums)
k = 2

new_nums = [-1, -1, -1, -1, -1]

for index in range(len(nums)):
    temp_index = (index + k) % size
    #print(temp_index)
    new_nums[temp_index] = nums[index]


for index in range(len(new_nums)):
    print(new_nums[index], end= " ")
print()

# 1.. (0 + 2) % 5 = 2 % 5 = 2
# 2.. (1 + 2) % 5 = 3 % 5 = 3
# 3.. (2 + 2) % 5 = 4 % 5 = 4
# 4.. (3 + 2) % 5 = 5 % 5 = 0
# 5.. (4 + 2) % 5 = 6 % 5 = 1
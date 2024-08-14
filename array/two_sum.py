nums = [1, 2, 3, 4, 5, 6, 8]
target = 9

start = 0
end = len(nums) - 1

while (start < end):
    if nums[start] + nums[end] == target:
        print(f"true:: {start, end}")
        break
    elif nums[start] + nums[end] < target:
        start += 1
    else:
        end -= 1

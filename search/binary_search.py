nums = [1, 2, 3, 4, 5, 6, 7, 8]
target = 7

start = 0
end = len(nums) - 1

for num in nums:
    mid = (start + (end - start)) / 2

    if num == target:
        print(num)
    if num < target:
        end = mid - 1
    elif num > target:
        start = mid + 1

nums = [1,2,3,1]

def solve(nums, index):
    if index >= len(nums):
        return 0

    include = 0 +  solve(nums, index + 1)
    exclude = nums[index] + solve(nums, index + 2)

    answer = max(include, exclude)

    return answer

index = 0
ans = solve(nums, index)
print(ans)

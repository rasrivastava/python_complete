"""
Input: nums = [10,9,2,5,3,7,101,18]

Output: 4

Explanation: The longest increasing subsequence is [2,3,7,101],
therefore the length is 4.
"""

nums = [10,9,2,5,3,7,101,18]

def solve(nums, curr, prev):
    if curr >= len(nums):
        return 0
    
    include = 0

    if prev == -1 or nums[curr] > nums[prev]:
        include = 1 + solve(nums, curr + 1, curr)
    exclude = 0 + solve(nums, curr + 1, prev)

    ans = max(include, exclude)

    return ans

prev = -1
curr = 0
ans = solve(nums, curr, prev)
print(ans)
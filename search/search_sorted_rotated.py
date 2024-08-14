nums = [4, 5, 6, 7, 1, 2, 3]

target = 6

start = 0
end = len(nums) - 1

while (start <= end):
    mid = (start + end) // 2
    
    # Check if the target is found
    if (target == nums[mid]):
        print(mid)
        break
    
    # determine which side is sorted

    if (nums[start] <= nums[mid]): # left is sorted
        if (nums[start] <= target < nums[mid]):
            end = mid - 1
        else:
            start = mid + 1
    else:
        if (nums[mid] < target <= nums[end]): # Right side is sorted
            start = mid + 1
        else:
            end = mid - 1

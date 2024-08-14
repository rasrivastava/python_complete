nums = [40, 50, 60, 10, 20, 30]
target = 30

start = 0
end = len(nums) - 1

while(start <= end):
    mid = (start + end) // 2

    if (target == nums[mid]):
        print(mid)
        break
    
    # Check if the left half is sorted
    if (nums[start] <= nums[mid]):
        if (nums[start] <= target < nums[mid]):
            end = mid - 1
        else:
            start = mid + 1
    #elif nums[mid] < nums[end]:
    else:
        if (nums[mid] < target <= nums[end]):
            start = mid + 1
        else:
            end = mid - 1

# while (start <= end):
#     mid = (start + end) // 2
    
#     # Check if the target is found
#     if (target == nums[mid]):
#         print(mid)
#         break
    
#     # determine which side is sorted

#     if (nums[start] <= nums[mid]): # left is sorted
#         if (nums[start] <= target < nums[mid]):
#             end = mid - 1
#         else:
#             start = mid + 1
#     else:
#         if (nums[mid] < target <= nums[end]): # Right side is sorted
#             start = mid + 1
#         else:
#             end = mid - 1

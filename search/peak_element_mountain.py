nums = [0, 2, 3, 4, 5, 4, 3, 2, 1]

start = 0
end = len(nums) - 1

while (start <= end):
    mid = (start + end) // 2
    
    # Check if mid is a peak element
    if (mid < len(nums) - 1 and mid > 0 and nums[mid] > nums [mid+1] and nums[mid-1] < nums[mid]):
        print(nums[mid])
        break
    # If mid is less than its next element, peak is to the right
    elif (mid < len(nums) - 1 and nums[mid] < nums [mid+1]):
        start = mid + 1
    # If mid is less than its previous element, peak is to the left
    elif (mid > 0 and nums[mid-1] > nums[mid]):
        end = mid - 1
    # Handle cases where mid is at the boundary
    else:
        if (mid == 0 and nums[mid] > nums[mid+1]):
            print(nums[mid]) # Peak at the start
            break
        if (mid == len(nums) - 1 and nums[mid-1] < nums[mid]):
            print(nums[mid]) # Peak at the end
            break
else:
    print("peak element is not found")
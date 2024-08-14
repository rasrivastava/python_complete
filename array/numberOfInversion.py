nums = [8, 4, 2, 1]
count = 0

for i in range(len(nums)):
    for j in range(i, len(nums)):
        if nums[i] > nums [j]:
           nums[j], nums[i] = nums[i], nums[j]
           count += 1

print(nums) # [1, 2, 4, 8] --> complexity O(n ^ 2)
print(count) # 6

### option 2

def merge_sort(arr):
    # If the array has one or zero elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Divide: Find the middle of the array
    mid = len(arr) // 2
    
    # Recursively sort the two halves
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    # Combine: Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    left_index, right_index = 0, 0
    
    # Merge the two lists while there are elements in both
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1
    
    # If there are remaining elements in left or right, append them
    if left_index < len(left):
        sorted_list.extend(left[left_index:])
    if right_index < len(right):
        sorted_list.extend(right[right_index:])
    
    return sorted_list

# Example usage:
nums = [8, 4, 2, 1]
sorted_arr = merge_sort(nums)
print(sorted_arr) # [1, 2, 4, 8]

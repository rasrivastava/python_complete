def merge_sort(arr):
    # Base case: a list of zero or one elements is already sorted
    if len(arr) <= 1:
        return arr

    # Find the midpoint of the list to divide it into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]  # Left half of the list
    right_half = arr[mid:]  # Right half of the list

    # Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the sorted halves together
    return merge(left_sorted, right_sorted)

def merge(left, right):
    sorted_arr = []  # List to store the merged result
    i = j = 0  # Pointers for left and right sublists

    # Compare elements from both sublists and merge them in order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])  # Add the smaller element to the sorted list
            i += 1  # Move the pointer in the left sublist
        else:
            sorted_arr.append(right[j])  # Add the smaller element to the sorted list
            j += 1  # Move the pointer in the right sublist
    """
    Left Sublist: [2, 5, 7]
    Right Sublist: [1, 3, 8, 9]
    Main Merging Loop:

    Compare 2 (left) and 1 (right): 1 is smaller, so append 1.
    Compare 2 (left) and 3 (right): 2 is smaller, so append 2.
    Compare 5 (left) and 3 (right): 3 is smaller, so append 3.
    Compare 5 (left) and 8 (right): 5 is smaller, so append 5.
    Compare 7 (left) and 8 (right): 7 is smaller, so append 7.
    End of Main Loop:

    At this point, the left sublist is exhausted. Only [8, 9] remains in the right sublist.
    """
    # Add any remaining elements from the left sublist
    sorted_arr.extend(left[i:])
    # Add any remaining elements from the right sublist
    sorted_arr.extend(right[j:])

    return sorted_arr  # Return the merged and sorted list

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)  # Output the sorted array

"""
The provided code implements the Merge Sort algorithm, which is a classic example of
the divide-and-conquer strategy. Here's a step-by-step explanation of the flow:


1. Initial Call to merge_sort

The function merge_sort is initially called with the array [38, 27, 43, 3, 9, 82, 10].

- Check for Base Case: 
    - The first thing merge_sort does is check if the length of the array is 1 or less. 
    - If so, the array is already sorted, and it is returned as is. In this case,
      the length is greater than 1, so we proceed.


2. Divide the Array

- Find the Midpoint: The array is divided into two halves using the midpoint.
- Midpoint (mid) = len(arr) // 2 = 7 // 2 = 3.
- Left Half: left_half = arr[:3] = [38, 27, 43].
- Right Half: right_half = arr[3:] = [3, 9, 82, 10].


3. Recursively Sort Both Halves

- The function then recursively sorts both the left and right halves.

- Sorting the Left Half [38, 27, 43]

- Divide Again:
- Midpoint (mid) = 3 // 2 = 1.
- Left: left_half = [38].
- Right: right_half = [27, 43].

- Base Case for [38]: The left half [38] has only one element, so it is returned as is.

- Sort the Right Half [27, 43]:
- Divide Again:
- Midpoint (mid) = 2 // 2 = 1.
- Left: left_half = [27].
- Right: right_half = [43].

- Base Cases for [27] and [43]: Both halves have only one element, so they are returned as is.

- Merge [27] and [43]:
- Compare the first elements of both lists: 27 < 43. <=========

- The merged and sorted result is [27, 43].  <=========
- Merge [38] and [27, 43]:     <=========

- Compare: 27 < 38 → Add 27.
- Compare: 38 < 43 → Add 38.
- Add the remaining element 43.
- The merged and sorted result is [27, 38, 43].
- Sorting the Right Half [3, 9, 82, 10]

- Divide Again:
Midpoint (mid) = 4 // 2 = 2.
Left: left_half = [3, 9].
Right: right_half = [82, 10].
Sort the Left Half [3, 9]:
Divide Again:
Midpoint (mid) = 2 // 2 = 1.
Left: left_half = [3].
Right: right_half = [9].
Base Cases for [3] and [9]: Both halves have only one element, so they are returned as is.
Merge [3] and [9]:
Compare: 3 < 9.
The merged and sorted result is [3, 9].
Sort the Right Half [82, 10]:
Divide Again:
Midpoint (mid) = 2 // 2 = 1.
Left: left_half = [82].
Right: right_half = [10].
Base Cases for [82] and [10]: Both halves have only one element, so they are returned as is.
Merge [82] and [10]:
Compare: 10 < 82.
The merged and sorted result is [10, 82].
Merge [3, 9] and [10, 82]:
Compare: 3 < 10 → Add 3.
Compare: 9 < 10 → Add 9.
Compare: 10 < 82 → Add 10.
Add the remaining element 82.
The merged and sorted result is [3, 9, 10, 82].


4. Merge the Two Halves

Now that both halves [27, 38, 43] and [3, 9, 10, 82] are sorted, they are merged together.
Merge [27, 38, 43] and [3, 9, 10, 82]:
Compare: 3 < 27 → Add 3.
Compare: 9 < 27 → Add 9.
Compare: 10 < 27 → Add 10.
Compare: 27 < 82 → Add 27.
Compare: 38 < 82 → Add 38.
Compare: 43 < 82 → Add 43.
Add the remaining element 82.
The final sorted result is [3, 9, 10, 27, 38, 43, 82].


5. Output the Sorted Array

The merge_sort function returns the fully sorted array [3, 9, 10, 27, 38, 43, 82], which is printed.

Summary

- The array is recursively divided into smaller parts until each part contains a single element.
- These parts are then merged back together in a sorted order.
- The final output is a sorted array, achieved through this recursive divide-and-conquer process.
"""
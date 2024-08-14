def find_pairs(nums, k):
    # Edge case: If k is negative, return 0 because no pairs can have a negative difference
    if k < 0:
        return 0

    # Initialize a set to keep track of numbers we've seen so far
    seen = set()
    # Initialize a set to keep track of unique k-diff pairs
    pairs = set()

    # Iterate through each number in the list
    for num in nums:
        # Check if there's a number that, when added to k,
        # gives us a pair with the current number
        if num + k in seen:
            # Add the pair (num, num + k) to the pairs set (order doesn't matter)
            pairs.add((num, num + k))

        # Check if there's a number that, when subtracted by k,
        # gives us a pair with the current number
        if num - k in seen:
            # Add the pair (num - k, num) to the pairs set
            pairs.add((num - k, num))

        # Add the current number to the seen set
        seen.add(num)

    # The length of the pairs set gives us the number of unique k-diff pairs
    print(pairs)
    return len(pairs)

# Example usage
nums1 = [3, 1, 4, 1, 5]
k1 = 2
print(find_pairs(nums1, k1))  # Output: 2 ## {(1, 3), (3, 5)}

nums2 = [1, 2, 3, 4, 5]
k2 = 1
print(find_pairs(nums2, k2))  # Output: 4 ## {(2, 3), (4, 5), (1, 2), (3, 4)}

nums3 = [1, 3, 1, 5, 4]
k3 = 0
print(find_pairs(nums3, k3))  # Output: 1 ## {(1, 1)}

nums3 = [1, 3, 1, 5, 4, 4]
k3 = 0
print(find_pairs(nums3, k3))  # Output: 2 ## {(4, 4), (1, 1)}

# nums = [2,3,6,7]
# target = 7

# main_sum_list = []

# for i in range(len(nums)):
#     sum = 0
#     for j in range(len(nums)):
#         sum_list = []
#         if i <= j:
#             for num in nums[i:j+1]:
#                 sum = sum + num
#                 sum_list.append(num)
#                 if sum == target:
#                     #print(sum_list)
#                     main_sum_list.append(sum_list)

# print(main_sum_list) # [[2, 3], [7]]


## second method

def combinationSum(candidates, target):
    # Initialize a list to store combinations that sum up to the target
    result = []

    # Initialize a list for storing the current list of combinations
    current_combinations = [[]]

    # Iterate over each candidate
    for candidate in candidates:
        # For each existing combination, add the candidate to it
        for comb in current_combinations:
            new_sum = sum(comb) + candidate
            # Continue only if adding the candidate doesn't exceed the target
            if new_sum <= target:
                new_comb = comb + [candidate]
                # If the new sum matches the target, add the combination to the result
                if new_sum == target:
                    result.append(new_comb)
                # Otherwise, add the new combination to the list for further processing
                else:
                    current_combinations.append(new_comb)

    return result

# Example usage:
candidates = [2, 3, 6, 7]
target = 7
print(combinationSum(candidates, target))  # Output: [[2, 2, 3], [7]]


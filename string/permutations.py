#my_set = [1, 2, 3, 4, 5]
# my_set = [1, 2, 3]

# # current
# current = my_set[1]
# #print(current)

# # print(my_set[:1])   # [1]
# # print(my_set[1+1:]) # [3, 4, 5]

# remaining = my_set[:1] + my_set[1+1:] # [1, 3, 4, 5]

# #print(remaining)

# ll = []

# ll.append([current] + remaining)
# print(ll)

# s = [1, 2, 3]
# permutations = []
# stack = []

# for i in range(len(s)):
#     current = [s[i]]
#     remaining = s[:i] + s[i+1:]
#     stack.append((current, remaining))

# while stack:
#     print("=================== START ==================================")
#     print("------------------------------")
#     for element in stack:
#         print(element)
#         # ([1], [2, 3])
#         # ([2], [1, 3])
#         # ([3], [1, 2]) --> POPED OUT

#         # ([1], [2, 3])
#         # ([2], [1, 3])
#         # ([3, 1], [2]) --> newly added
#         # ([3, 2], [1]) --> newly added
#     print("------------------------------")
#     current, remaining = stack.pop() # ([3], [1, 2]) --> ([3, 2], [1])
#     print("- current -> ", current)     # [3]        --> [3, 2]
#     print("- remaining -> ", remaining) # [1, 2]     --> [1]

#     if len(remaining) == 0:
#         print("-->--> ", current)
#         permutations.append(current)
#     else:
#         for i in range(len(remaining)):
#             new_current = current + [remaining[i]] #                      --> current => [3, 2] ; [remaining[i]] => [1] ==> [3, 2, 1]
#             new_remaining = remaining[:i] + remaining[i+1:] #             --> remaining[:i] => [1]
#             print("- new_current ->", new_current)     # [3, 1] -> [3, 2] --> [3, 2, 1]
#             print("- new_remaining ->", new_remaining) # [2]    -> [1]    --> []
#             stack.append((new_current, new_remaining))
# print("=================== END ==================================")
# print(permutations)

s = [1, 2, 3]          # The initial list for which we want to generate permutations
stack = []             # Stack to hold pairs of (current permutation, remaining elements)
permutations = []      # List to store all the generated permutations

# Initial population of the stack with the first level of permutations
for i in range(len(s)):
    current = [s[i]]   # Start the current permutation with the i-th element
    remaining = s[:i] + s[i+1:]  # Get the remaining elements after removing the i-th element
    stack.append((current, remaining))  # Push the pair (current, remaining) onto the stack
    print(stack)
    """
    [([1], [2, 3])]
    [([1], [2, 3]), ([2], [1, 3])]
    [([1], [2, 3]), ([2], [1, 3]), ([3], [1, 2])]
    """

# Process the stack until it's empty
while stack:
    current, remaining = stack.pop()  # Pop the last element from the stack

    if len(remaining) == 0:  # If no elements are remaining, we've completed a permutation
        permutations.append(current)  # Add the completed permutation to the list
    else:
        # Generate new permutations by choosing each of the remaining elements
        for i in range(len(remaining)):
            new_current = current + [remaining[i]]  # Add the current element to the permutation
            new_remaining = remaining[:i] + remaining[i+1:]  # Remove the selected element from the remaining ones
            stack.append((new_current, new_remaining))  # Push the new pair (new_current, new_remaining) onto the stack

print(permutations)  # Print all generated permutations

# The code uses a stack-based approach to generate all permutations of the list s.

# Initially, the stack is populated with the first level of permutations by fixing one element and leaving the rest for further permutations.

# The while loop then continues to pop elements from the stack, generating new permutations
# until all possibilities are exhausted.

# The permutations list holds the final result, which contains all possible permutations of s.

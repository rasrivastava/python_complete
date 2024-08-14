# List of strings
strings = ["flower", "flow", "flight"]

# Check if the list is empty
if not strings:
    longest_common_prefix = ""
else:
    # Initialize the prefix with the first string in the list
    prefix = strings[0]

    # Iterate over the remaining strings
    for string in strings[1:]:
        # Continue reducing the prefix until it matches the start of the current string
        while not string.startswith(prefix):
            # Remove the last character from the prefix
            prefix = prefix[:-1]
            # If prefix is empty, there is no common prefix
            if not prefix:
                break
    
    longest_common_prefix = prefix

# Print the longest common prefix
print(longest_common_prefix)  # Output: "fl"


# def longest_common_prefix(strs):
#     # Check if the list is empty
#     if not strs:
#         return ""

#     # Initialize the prefix with the first string in the list
#     prefix = strs[0]

#     # Iterate over the remaining strings
#     for string in strs[1:]:
#         # Continue reducing the prefix until it matches the start of the current string
#         while not string.startswith(prefix):
#             # Remove the last character from the prefix
#             prefix = prefix[:-1]
#             # If prefix is empty, return immediately as there's no common prefix
#             if not prefix:
#                 return ""

#     # Return the longest common prefix found
#     return prefix

# # Example usage
# strings = ["flower", "flow", "flight"]
# print(longest_common_prefix(strings))  # Output: "fl"

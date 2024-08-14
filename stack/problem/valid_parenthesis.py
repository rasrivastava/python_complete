# test_string = "[abc[abc]]"
# test_string_2 = "[abc[ab[c]]"
# test_string_3 = "[[][][][]]"
# test_string_4 = "[[[[]]]"
# test_string_5 = "[[[[]]]]"

# stack = []

# for ch in test_string:
#     if ch == "[":
#         stack.append(ch)
#     else:
#         if ch == "]" and stack[-1] == "[":
#             stack.pop()

# if stack:
#     print("Invalid")
# else:
#     print("Valid")

def isValid(s: str) -> bool:
    # Define a mapping of closing brackets to their corresponding opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []  # Initialize an empty stack to keep track of opening brackets
    
    # Iterate through each character in the string
    for char in s:
        if char in bracket_map:
            # If the character is a closing bracket
            if stack:  # Check if the stack is not empty
                top_element = stack.pop()  # Pop the top element from the stack
            else:
                top_element = '#'  # Use a dummy value if the stack is empty
            
            # Check if the popped element matches the expected opening bracket
            if bracket_map[char] != top_element:
                return False  # Return False if there's a mismatch
        else:
            # If it's an opening bracket, push it onto the stack
            stack.append(char)
    
    # If the stack is empty, all brackets were properly closed; otherwise, return False
    return not stack


print(isValid("()"))       # Output: True
print(isValid("()[]{}"))   # Output: True
print(isValid("(]"))       # Output: False

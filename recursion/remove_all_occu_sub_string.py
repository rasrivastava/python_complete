# sinlge occurance
s1 = "aabbccabcaabbccsd"

part = "abc"

result = s1.replace(part, "")

print(result)

# ----------------------------------------------------

# multiple occurance
s1 = "aabbccabcaabbccsd"
part = "abc"

while part in s1:
    s1 = s1.replace(part, "")

print(s1)

# -------------------------------------------------------

s1 = "aabbccabcaabbccsd"
part = "abc"

result = []
i = 0

while (i < len(s1)):
    # Check if the substring starting at the current index matches 'part'
    if s1[i:i + len(part)] == part:
        # Skip the length of 'part'
        i = i + len(part)
    else:
        # Append the current character to the result
        result.append(s1[i])
        i = i + 1

result = "".join(result)

print(result)

########################
###  using recusion  ###
########################

def helper(s1, part):
    # base case
    # Base case: If the string is empty or shorter than the part, return it as is
    if len(s1) < len(part):
        return s1
    
    # If the part is found at the beginning of the string
    if s1.startswith(part):
        # Recursively call on the remainder of the string after removing the part
        return helper(s1[len(part):], part)
    else:
        # Otherwise, take the first character and proceed recursively with the rest
        return s1[0] + helper(s1[1:], part)

s1 = "aabbccabcaabbccsd"
part = "abc"

helper(s1, part)

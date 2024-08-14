"""
Input: [4, 5, 2, 25]
Output: [5, 25, 25, -1]
"""

arr = [4, 5, 2, 25]

stack = []

result = [-1] * len (arr)

for i in range(len(arr)):
        # While stack is not empty and the current element is greater
        # than the element corresponding to the index on the top of the stack
        while stack and arr[i] > arr[stack[-1]]:
            # Update the result for the index at the top of the stack
            index = stack.pop()
            result[index] = arr[i]
        
        # Push the current element's index onto the stack
        stack.append(i)

print(result)

# 1. {4} element and [0] index
# while stack and arr[i] > arr[stack[-1]]: --> false as stack is empty
#    stack --> [0]

# 2. {5} element and [1] index
#  while stack and arr[i] > arr[stack[-1]]: --> true stack is not empty
#  index = stack.pop()  --> index = 0 --> stack is empty
#  result[index] = arr[i] --> result[0] = arr[1] --> 5 ==> result[0] = 5
#  while stack and arr[i] > arr[stack[-1]]: --> true stack is not empty
#  stack.append(i) --> stack --> push 1

# 3. {2} element and [2] index
# while stack and arr[i] > arr[stack[-1]]: --> false as stack is empty
# arr[i] > arr[stack[-1]] ==> arr[2] > arr[1] ==> 2 > 5 ==> false
# stack.append(i) ==> stack = [1,  2]

# 4. {25} element and [3] index
# while stack and arr[i] > arr[stack[-1]]: --> true stack is not empty
# index = stack.pop() --> index = 2
# result[index] = arr[i] ==> result[2] = arr[3] ==> result[2] = 25


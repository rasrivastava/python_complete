# arr = [1, 2, 3]

# n = len(arr)

# for i in range(n):
#     for j in range(i, n):
#         print(arr[i:j+1])


def generate_subarrays(arr, start, end):
    # Base case: if start index reaches the end of the array, return
    if start == len(arr):
        return
    
    # If the end index exceeds the length, reset it to start + 1 and increment start
    elif end > len(arr):
        generate_subarrays(arr, start + 1, start + 1)
    
    # Recursive case
    else:
        # Print the current subarray
        if start < end:
            print(arr[start:end])
        
        # Recur with the next end index
        generate_subarrays(arr, start, end + 1)

# Example usage
arr = [1, 2, 3]
generate_subarrays(arr, 0, 1)

# s1 = [1, 2, 3]

# print(s1[1:]) # [2, 3]
# print(s1[:1]) # [1]
# print(s1[1:2]) # [2]

# print("----------")
# print(s1[0:0])  # [1]
# print(s1[0:1])  # [1]
# print(s1[0:2])  # [1, 2]
# print(s1[0:3])  # [1, 2, 3]
# print("----------")

for i in range(len(s1)):
    for j in range(i, len(s1)):
        #print(f"{i}:{j} || {s1[i:j+1]}")
        print(s1[i:j+1])

# 1.  -> for i in range(len(s1))              --> 0 - 3 
# 1.a -> for j in range(i, len(s1))           --> 0 - 3
# 1.b -> print(s1[i:j+1])          |i=0|j=0|  --> s1[i:j+1] --> s1[0:1] --> [1]
# 1.b -> print(s1[i:j+1])          |i=0|j=1|  --> s1[i:j+1] --> s1[0:2] --> [1, 2]
# 1.b -> print(s1[i:j+1])          |i=0|j=2|  --> s1[i:j+1] --> s1[0:3] --> [1, 2, 3]

# 2.  -> for i in range(len(s1))              --> 1 - 3 
# 2.a -> for j in range(i, len(s1))           --> 1 - 3
# 2.b -> print(s1[i:j+1])          |i=1|j=1|  --> s1[i:j+1] --> s1[1:2] --> [2]
# 2.b -> print(s1[i:j+1])          |i=1|j=2|  --> s1[i:j+1] --> s1[1:3] --> [2, 3]

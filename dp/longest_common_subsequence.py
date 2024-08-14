"""
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
"""


text1 = "abcde"
text2 = "ace"

def solve(text1, text2, i, j):
    if len(text1) <= i or len(text2) <= j:
        return 0
    
    ans = 0

    if text1[i] == text2[j]:
        ans = 1 + solve(text1, text2, i + 1, j + 1)
    else:
        ans = 0 + max(solve(text1, text2, i + 1, j),
                      solve(text1, text2, i, j + 1))
    
    return ans

i = 0
j = 0
ans = solve(text1, text2, i, j)
print(ans)

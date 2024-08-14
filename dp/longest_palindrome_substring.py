"""
Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".


Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
"""

def solve(s1, s2, i, j):
    if i >= len(s1) or j >= len(s2):
        return 0
    
    ans = 0

    if s1[i] == s2[j]:
        ans = 1 + solve(s1, s2, i + 1, j + 1)
    else:
        ans = 0 + max(solve(s1, s2, i + 1, j),
                      solve(s1, s2, i, j + 1))
    
    return ans


s1 = "bbbab"
s2 = s1[::-1]
i = 0
j = 0

ans = solve(s1, s2, i, j)
print(ans)
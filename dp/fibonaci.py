num = 6

# normal recursion
def recursion(num):
    # base condition
    if num == 0 or num == 1:
        return num
    ans = recursion(num - 1) + recursion(num - 2)
    return ans

# using dp
def recursionUsingDp(num, dp):
    # base condition
    if num == 0 or num == 1:
        return num

    if dp[num] != -1:
        return dp[num]

    dp[num] = recursionUsingDp(num - 1, dp) + recursionUsingDp(num - 2, dp)
    return dp[num]

dp = [-1 for _ in range(num + 1)]
final_ans = recursionUsingDp(num, dp)
print(final_ans)

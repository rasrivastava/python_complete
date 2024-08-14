import sys
INT_MAX = sys.maxsize

coins = [1, 2, 5]
amount = 11

def solve(coins, amount):
    if amount <= 0:
        return 0
    
    final_answer = INT_MAX

    for index in range(len(coins)):
        if (amount - coins[index] >= 0):
            recur_ans = solve(coins, amount - coins[index])
            if recur_ans != INT_MAX:
                ans = 1 + recur_ans
                final_answer = min(ans, final_answer)
    return final_answer

ans = solve(coins, amount)
print(ans)

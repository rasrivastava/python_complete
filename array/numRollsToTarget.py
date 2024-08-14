n = 2 # The number of dice.
k = 6 # The number of faces on each die.
target = 7 # The target sum we want to achieve by rolling the dice.

MOD = 10**9 + 7

# Initialization: We initialize a 2D array dp where dp[i][j] represents
# the number of ways to get sum j using i dice.

# Create a 2D dp array initialized to 0
# There is exactly one way to achieve a sum of 0 with 0 dice, 
# which is by not rolling any dice at all. Hence, dp[0][0] = 1.
dp = []

for i in range(n + 1):
    row = [0] * (target + 1)
    dp.append(row)

print(dp) # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# Base case: one way to achieve sum 0 with 0 dice
dp[0][0] = 1

# Fill the dp table iteratively

# Iterates over the number of dice from 1 to n.
# i represents the current number of dice being considered. 
# We'll fill out the table row by row, where each row corresponds to a different number of dice. 
for i in range(1, n+1): # i is the number of dice
    #  Iterates over all possible sums from 1 to target.
    # j represents the current target sum we are trying to achieve with i dice.
    for j in range(1, target + 1): # # j is the current target sum
        # We start with the assumption that there are 0 ways to achieve the 
        # sum j with i dice and then update this value based on the possible face values.
        dp[i][j] = 0
        # Iterates over all possible face values of the dice from 1 to k.
        for x in range(1, k + 1): # x is the face value of the dice
            # If j - x >= 0, it means it's possible to achieve the sum j by first achieving the 
            # sum j - x with one less die (i.e., i-1 dice). This ensures that we don't access 
            # negative indices or invalid sums.
            if (j - x) >= 0:
                # This expression refers to the number of ways to achieve the sum j - x using i - 1 dice.
                dp[i][j] = (dp[i][j] + dp[i - 1][j - x]) % MOD

print(dp[n][target])

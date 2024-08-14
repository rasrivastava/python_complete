"""
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""

prices = [7, 1, 5, 3, 6, 4]

#min_price = float('inf')
min_price = 2**31 - 1 # This is the maximum value for a 32-bit signed integer
max_profit = 0

for price in prices:
    # Update min_price if the current price is lower
    if price < min_price:
        min_price = price
    # Calculate the profit by subtracting min_price from the current price
    profit = price - min_price
    # Update max_profit if the current profit is greater than the previous max_profit
    if profit > max_profit:
        max_profit = profit

print(max_profit)


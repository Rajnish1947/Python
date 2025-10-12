#  Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


def stockBuyandSell(prices):
    minimum_price = prices[0]
    profit = 0
    
    for i in range(1, len(prices)):
        current_profit = prices[i] - minimum_price
        if current_profit>profit:
            profit=current_profit
     
        minimum_price = min(minimum_price, prices[i])
    
    return profit

# Test
prices = [7, 1, 5, 3, 6, 4]
print(stockBuyandSell(prices))  # Output: 5
     
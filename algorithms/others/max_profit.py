# Best Time to Buy a Stock

# version 1: one can only make one transaction
def get_max_profit1(prices):
    # keep record of the minimum so far
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit


# version 2: one can make as many transactions
def get_max_profit2(prices):
    # just add it to max_profit when prices[i+1] - prices[i]
    pass


# version 3: one can only make two transactions
# brute force: find the max profit of prices[:i] then the max profit of prices[i:]
# optimization: use one arrays to record the max profit of prices[:i] for each i
# and another array to record the max profit of prices[i:] for each i (DP)
def get_max_profit3(prices):
    if not prices:
        return 0
    profits = [0] * len(prices)
    # max profit of prices[:i] for each i
    max_profit_left = 0
    min_price = prices[0]
    for i in range(1, len(prices)):
        min_price = min(min_price, prices[i])
        max_profit_left = max(max_profit_left, prices[i] - min_price)
        profits[i] = max_profit_left
    # max profit of prices[i:] for each i
    max_profit_right = 0
    max_price = prices[-1]
    for i in range(len(prices) - 1, 0, -1):
        max_price = max(max_price, prices[i])
        max_profit_right = max(max_profit_right, max_price - prices[i])
        profits[i] += max_profit_right
    
    return max(profits)
# O(n) time and space
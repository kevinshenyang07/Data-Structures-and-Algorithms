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
    pass


# version 3: one can only make two transactions
# brute force: find the max profit of prices[:i] then the max profit of prices[i:]
# optimization: use one arrays to record the max profit of prices[:i] for each i
# and another array to record the max profit of prices[i:] for each i (DP)
def get_max_profit3(prices):
    pass

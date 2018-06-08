# v1
# can only buy then sell once
def max_profit_1(prices):
    if not prices or len(prices) < 2:
        return 0

    low = prices[0]  # lowest price so far
    profit = 0
    for price in prices:
        if low >= price:
            low = price
        else:
            profit = max(profit, price - low)
    return profit
# O(n) time and space


# v3
# can only buy then sell twice
# brute force: find the max profit of prices[:i] then the max profit of prices[i:]
# optimization: use an array to record the max profit of prices[:i] for each i
# and another array to record the max profit of prices[i:] for each i (DP)
def max_profit_3(prices):
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

# v4
# can only buy then sell for k times
#

# with cooldown (cannot buy after the day sold)
# assume all prices are non-negative
def max_profit_cooldown(prices):
    '''
    1) state definition
    hold[i]: max profit when holding a position on day i
    unhold[i]: max profit not holding a position on day i

    2) base cases:
    hold[0] = -prices[0]
    hold[1] = max(-prices[0], -prices[1])
    unhold[0] = 0
    unhold[1] = max(0, hold[0] + prices[1])

    3) state transfer function:
    hold[i] = max(hold[i-1],                # not buying on day i
                  unhold[i-2] - prices[i])  # buying on day i
    unhold[i] = max(unhold[i-1],            # no position on day i-1
                    hold[i-1] + prices[i])  # hold a position on dy i-1 and sell on day i
    '''
    if not prices or len(prices) < 2:
        return 0

    hold = [0] * len(prices)
    unhold = [0] * len(prices)

    hold[0] = -prices[0]
    hold[1] = max(-prices[0], - prices[1])
    unhold[1] = max(0, hold[0] + prices[1])

    for i in range(2, len(prices)):
        hold[i] = max(hold[i-1], unhold[i-2] - prices[i])
        unhold[i] = max(unhold[i-1], hold[i-1] + prices[i])

    return unhold[-1]
# O(3 ^ n) for brute force
# O(n) time and space
# space can be optimized to O(1)

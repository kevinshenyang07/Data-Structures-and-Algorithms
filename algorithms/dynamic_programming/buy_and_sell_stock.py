# v1

# v2

# v3

# v4

# with Cooldown
# assume all prices are non-negative
def max_profit(prices):
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

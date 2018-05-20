# Coin Change II
def change(amount, coins):
    '''
    dp[i][j] is the number of ways to make change to amount j with first i coins

    dp[i][j] = 0                                 i = 0, j > 0
             = 1                                 j = 0
             = dp[i-1][j]                        j < coins[i-1]
             = dp[i-1][j] + dp[i][j-coins[i-1]]  j >= coins[i-1]
    '''
    dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
    for i in range(len(coins) + 1):
        dp[i][0] = 1

    for i in range(1, len(coins) + 1):
        for j in range(1, amount + 1):
            dp[i][j] = dp[i-1][j]
            if j >= coins[i-1]:
                dp[i][j] += dp[i][j-coins[i-1]]

    return dp[-1][-1]


def change_optimized(amount, coins):
    dp = [0 for _ in range(amount + 1)]
    dp[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i-coin]

    return dp[-1]

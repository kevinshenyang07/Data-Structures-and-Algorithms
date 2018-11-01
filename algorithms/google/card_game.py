# given a pile of cards represented as array of integers (points)
# two players take turn to draw 1 to 3 cards from the right end
# returns the highest score the either player
def max_score(points):
    """
    dp[i]: the max score of current player choosing from arr[:i+1]
    dp[0] = arr[0]
    dp[i] = max(sum(arr[:i+1]) - dp[i - k])  1 <= k <= 3
    """
    n = len(points)

    pre_sum = [0] * n
    pre_sum[0] = points[0]
    for i in range(1, n):
        pre_sum[i] = pre_sum[i - 1] + points[i]

    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for k in range(1, min(4, i + 1)):
            # dp[i-k] to be the best effort for player 2 to get higher score
            # choosing from arr[:i-k+1]
            dp[i] = max(dp[i], pre_sum[i - 1] - dp[i - k])
    # score of player 1 / 2
    return max(dp[-1], pre_sum[-1] - dp[-1])


if __name__ == '__main__':
    points = [2, 3, -1, 4, -2, 1, 6]
    print max_score(points)  # 11

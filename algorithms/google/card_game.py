# given a pile of cards represented as array of integers (points)
# two players take turn to draw 1 to 3 cards from the left end
# returns the highest score of either player
def max_score(points):
    """
    start from the base case when there're <= 3 cards (iterate from right to left)

    dp[i]: how much the current player can out-score the other player
           when it's the current player turn to pick from index i

    dp[n-i] = sum(points[n-i:])  1 <= i <= 3

    dp[i] = max(sum(points[i:i+k]) - dp[i+k])  1 <= k <= 3 (current player takes k cards)
    """
    if not points:
        return 0

    n = len(points)

    # pre_sum[k] = sum(points[:k])
    pre_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        pre_sum[i] = pre_sum[i - 1] + points[i - 1]

    dp = [float('-inf')] * n
    for k in range(1, min(4, n + 1)):
        dp[-k] = pre_sum[n] - pre_sum[n - k]

    for i in range(n - 4, -1, -1):
        for k in range(1, 4):
            curr_score = pre_sum[i + k] - pre_sum[i]
            dp[i] = max(dp[i], curr_score - dp[i + k])

    score_p1 = (dp[0] + pre_sum[n]) / 2
    score_p2 = score_p1 - dp[0]
    return max(score_p1, score_p2)


if __name__ == '__main__':
    print max_score([])  # 0
    print max_score([-1])  # 0
    print max_score([-1, 3, 2])  # 4
    print max_score([3, -2, 4])  # 5
    print max_score([2, 3, -1, 4])  # 5
    print max_score([2, 3, -1, 4, -2, 1, 6])  # 9
    print max_score([1, 3, -2, -5, 6, 4])  # 8
    print max_score([-1,-10,-2,-4,-2,-5])  # -12

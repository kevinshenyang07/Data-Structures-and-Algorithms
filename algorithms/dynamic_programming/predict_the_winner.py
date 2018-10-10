# Predict the Winner
# Given an array of scores that are non-negative integers, player 1 picks one of the numbers
# from either end of the array followed by the player 2 and then player 1 and so on.
# Each time a player picks a number, that number will not be available for the next player.
# This continues until all the scores have been chosen. The player with the maximum score wins.
# If both players have the same score, player 1 still wins. Predict if player 1 would win.
class SolutionV1(object):
    def PredictTheWinner(self, nums):
        """
        for 0 <= i, j < n, and i <= j, a window can be constructed

        dp[i][j]: how much the player who picks first can out-score the other

        dp[i][j] = i                                               if i == j
                 = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1]) if i != j

        dp[i + 1][j] / dp[i][j - 1]: the other player's best effort to out-score current player
        """
        n = len(nums)
        total_score = sum(nums)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = nums[i]

        for width in range(2, n + 1):
            for i in range(n - width + 1):
                j = i + width - 1
                # need to keep track of the balance to make correct counter-move
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])

        return dp[0][n - 1] >= 0


# followup on reducing space complexity: use only last two 'levels'
class SolutionV2(object):
    n = len(nums)
    total_score = sum(nums)
    dp = nums[:]

    for width in range(2, n + 1):
        for i in range(n - width + 1):
            j = i + width - 1
            # can overwrite since dp[i] is only related to dp[i] and dp[i + 1]
            dp[i] = max(nums[i] - dp[i + 1], nums[j] - dp[i])

    return dp[0] >= 0

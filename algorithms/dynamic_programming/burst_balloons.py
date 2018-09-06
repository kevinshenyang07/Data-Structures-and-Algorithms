# Burst Balloons
# dp[i][j]: max coins obtained by bursting balloons between i and j (exclusive)
# dp[i][j] = 0 if j - i < 2
# dp[i][j] = max(nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j] for i < k < j)
#               (all balloons between i and j are bursted except for the one on position k)
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        N = len(nums)
        dp = [[0] * N for _ in range(N)]

        for width in range(3, N + 1):
            for i in range(N - width + 1):
                j = i + width - 1

                for k in range(i + 1, j):
                    curr_coins = nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j]
                    dp[i][j] = max(dp[i][j], curr_coins)

        return dp[0][N-1]
# O(n^3) time, O(n^2) space

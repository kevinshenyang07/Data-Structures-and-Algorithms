# Maximal Square
# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# => 4
class Solution(object):
    def maximalSquare(self, matrix):
        """
        dp[i][j]: max length of the squares whose lower-right corners locate at (i-1, j-1)
        dp[i][0] = dp[0][j] = int(matrix[i][j])
        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1 if M[i-1][j-1] == '1'
                 = 0                                             if M[i-1][j-1] == '0'
        """
        if not any(matrix):
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        max_length = 0

        for i in range(m):
            dp[i][0] = int(matrix[i][0])
            max_length = max(max_length, dp[i][0])
        for j in range(n):
            dp[0][j] = int(matrix[0][j])
            max_length = max(max_length, dp[0][j])

        for i in range(1, m):
            for j in range(1, n):
                if int(matrix[i][j]):
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    max_length = max(max_length, dp[i][j])

        return max_length * max_length

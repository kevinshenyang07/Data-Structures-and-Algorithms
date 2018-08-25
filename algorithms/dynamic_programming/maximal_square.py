# Maximal Square
# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# => 4

# dp[i][j]: max length of the squares whose lower-right corners locate at (i-1, j-1)
# dp[i][0] = dp[0][j] = 0  (base case)
# dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1 if M[i-1][j-1] == '1'
#          = 0                                             if M[i-1][j-1] == '0'
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not any(matrix): return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_length = 0  # of a square

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i-1][j-1] == '1':
                    # smallest square guaranteed to be able to extend its length by one
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    max_length = max(max_length, dp[i][j])

        return max_length * max_length


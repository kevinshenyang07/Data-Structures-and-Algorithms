# Longest Increasing Path in a Matrix
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not any(matrix): return 0

        m, n = len(matrix), len(matrix[0])
        memo = [[0] * n for _ in range(m)]
        max_path = 1

        for i in range(m):
            for j in range(n):
                max_path = max(max_path, self.dfs(i, j, matrix, memo))

        return max_path

    def dfs(self, i, j, matrix, memo):
        if memo[i][j] > 0:  # already searched
            return memo[i][j]

        memo[i][j] = 1

        for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
                if matrix[i][j] < matrix[x][y]:
                    memo[x][y] = self.dfs(x, y, matrix, memo)
                    memo[i][j] = max(memo[i][j], memo[x][y] + 1)

        return memo[i][j]

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

        m, n = len(matrix), len(matrix[0])
        curr_path = 1

        for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
            if 0 <= x < m and 0 <= y < n and matrix[i][j] < matrix[x][y]:
                next_path = self.dfs(x, y, matrix, memo)
                curr_path = max(curr_path, 1 + next_path)

        memo[i][j] = curr_path
        return curr_path

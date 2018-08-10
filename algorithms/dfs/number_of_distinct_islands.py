# Number of Distinct Islands
# Count the number of distinct islands. An island is considered to be the same as another
# if and only if one island can be translated (and not rotated or reflected) to equal the other.
# Example:
# 11011
# 10000
# 00001
# 11011
# => 3
class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not any(grid):
            return 0

        m, n = len(grid), len(grid[0])
        paths = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    path = []
                    self.dfs(i, j, grid, path)
                    paths.add(''.join(path))

        return len(paths)

    def dfs(self, i, j, grid, path):
        grid[i][j] = 0
        for x, y, d in [(i - 1, j, 'u'), (i, j - 1, 'l'), (i + 1, j, 'd'), (i, j + 1, 'r')]:
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                path.append(d)
                self.dfs(x, y, grid, path)

        path.append('b')  # back to last level of recursion

# combine direction and recursion to form a string that present the path

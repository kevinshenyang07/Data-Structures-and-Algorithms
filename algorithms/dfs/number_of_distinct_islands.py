# Number of Distinct Islands
# Count the number of distinct islands. An island is considered to be the same as another
# if and only if one island can be translated (and not rotated or reflected) to equal the other.
# Example:
# 11011
# 10000
# 00001
# 11011
# => 3
# Approach:
# combine direction and recursion to form a string that present the path
class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not any(grid):
            return 0

        m, n = len(grid), len(grid[0])
        islands = set()
        directions = { 'u': (-1, 0), 'l': (0, -1), 'd': (1, 0), 'r': (0, 1) }

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    path = []
                    self.dfs(i, j, grid, path, directions)
                    islands.add(''.join(path))

        return len(islands)

    def dfs(self, x, y, grid, path, directions):
        m, n = len(grid), len(grid[0])
        grid[x][y] = 0

        for d in directions:
            dx, dy = directions[d]
            i, j = x + dx, y + dy

            if 0 <= i < m and 0 <= j < n and grid[i][j]:
                path.append(d)
                self.dfs(i, j, grid, path, directions)

        path.append('b')  # end of current recursion

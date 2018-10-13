class Solution(object):
    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(grid), len(grid[0])

        # -1: empty but hit; 0: empty
        # 1: unvisited / isolated; 2: connected
        for i, j in hits:
            grid[i][j] -= 1

        for j in range(n):
            if grid[0][j] == 1:
                self.dfs(0, j, grid)

        res = [0] * len(hits)

        for i in range(len(hits) - 1, -1, -1):
            x, y = hits[i]
            grid[x][y] += 1

            if grid[x][y] == 1 and self.is_connected(x, y, grid):
                res[i] = self.dfs(x, y, grid) - 1  # except for the hit point

        return res

    def dfs(self, i, j, grid):
        m, n = len(grid), len(grid[0])
        grid[i][j] = 2
        added = 1  # current brick

        for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                added += self.dfs(x, y, grid)  # nearby bricks

        return added

    def is_connected(self, i, j, grid):
        m, n = len(grid), len(grid[0])

        if i == 0 and 0 <= j < n and grid[i][j] == 1:
                return True

        for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 2:
                return True

        return False

# Number of Islands
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not any(grid):
            return 0
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(i, j, grid)
        return count

    def dfs(self, i, j, grid):
        m, n = len(grid), len(grid[0])
        grid[i][j] = '0'

        for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
            if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                self.dfs(x, y, grid)
# O(mn) time, O(max(m, n)) space for recursive stacks


# follow up: how to find the number of lakes?
# a lake is an area of water surrounded horizonatally and vertically
# by the same island

# solution:
# 1. use num_islands() to mark islands with different ids
# 2. iterate through the grid, if it's water then dfs to see if
#    it's surrounded by lands of the same id

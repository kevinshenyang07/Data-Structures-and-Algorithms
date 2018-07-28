# Bomb Enemy
# Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero),
# return the maximum enemies you can kill using one bomb.
# The bomb kills all the enemies in the same row and column from the planted point until it hits
# the wall since the wall is too strong to be destroyed.
# A bomb can only be placed at an empty cell.
# For the given grid:
# 0 E 0 0
# E 0 W E
# 0 E 0 0
# => return 3
class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not any(grid): return 0

        m, n = len(grid), len(grid[0])
        kills_curr_row = 0
        kills_by_col = [0] * n  # can be reused
        kills_max = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'W':
                    continue
                if j == 0 or grid[i][j-1] == 'W':
                    kills_curr_row = self.kills_on_row(grid, i, j)
                if i == 0 or grid[i-1][j] == 'W':
                    kills_by_col[j] = self.kills_on_col(grid, i, j)
                if grid[i][j] == '0':
                    kills_max = max(kills_max, kills_curr_row + kills_by_col[j])

        return kills_max

    # count kills for row i from column j, until hitting the wall
    def kills_on_row(self, grid, i, j):
        count = 0
        while j < len(grid[0]) and grid[i][j] != 'W':
            if grid[i][j] == 'E':
                count += 1
            j += 1
        return count

    # count kills for column j from row i, until hitting the wall
    def kills_on_col(self, grid, i, j):
        count = 0
        while i < len(grid) and grid[i][j] != 'W':
            if grid[i][j] == 'E':
                count += 1
            i += 1
        return count

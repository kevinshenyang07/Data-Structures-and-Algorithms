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
        row_hits = 0
        col_hits = [0] * n  # can be reused
        max_hits = 0

        for i in range(m):
            for j in range(n):
                # a wall on the left
                if j == 0 or grid[i][j-1] == 'W':
                    row_hits = self.curr_row_hits(grid, i, j)
                # a wall on the top
                if i == 0 or grid[i-1][j] == 'W':
                    col_hits[j] = self.curr_col_hits(grid, i, j)

                if grid[i][j] == '0':
                    max_hits = max(max_hits, row_hits + col_hits[j])

        return max_hits

    # count hits on row i starting from column j, until hitting the wall
    def curr_row_hits(self, grid, i, j):
        count = 0
        while j < len(grid[0]) and grid[i][j] != 'W':
            if grid[i][j] == 'E':
                count += 1
            j += 1
        return count

    # count hits on column j starting from row i, until hitting the wall
    def curr_col_hits(self, grid, i, j):
        count = 0
        while i < len(grid) and grid[i][j] != 'W':
            if grid[i][j] == 'E':
                count += 1
            i += 1
        return count
# O(mn) time, O(n) space
# the 2 inner loops will visit each cell at most twice => amortized O(1) inside

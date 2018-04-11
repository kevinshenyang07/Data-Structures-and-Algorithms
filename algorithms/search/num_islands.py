def num_islands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not any(grid):
            return 0
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                res += 1
                dfs(grid, i, j)
    return res


def dfs(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return
    if grid[i][j] == '1':
        # mark itself and all adj islands as 0
        grid[i][j] = '0'
        dfs(grid, i - 1, j)
        dfs(grid, i, j + 1)
        dfs(grid, i + 1, j)
        dfs(grid, i, j - 1)
# O(mn) time, O(max(m, n)) space for recursive stacks


# follow up: how to find the number of lakes?
# a lake is an area of water surrounded horizonatally and vertically
# by the same island

# solution:
# 1. use num_islands() to mark islands with different ids
# 2. iterate through the grid, if it's water then dfs to see if
#    it's surrounded by lands of the same id
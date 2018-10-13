from union_find import UnionFind

class Solution(object):
    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(grid), len(grid[0])
        # extra dummy node m * n to connect to all nodes in first row
        uf = UnionFind(m * n + 1)
        # mark all hits so that they won't be unioned initially
        for i, j in hits:
            if grid[i][j] == 1:
                grid[i][j] = 2
        # traversing the grid is slow, can improve it with dfs on hit points
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.union_around(i, j, grid, uf)
        # number of nodes connected to dummy node after all hits
        count = uf.counts[uf.find(m * n)]
        res = [0] * len(hits)
        # roll back
        for i in range(len(hits) - 1, -1, -1):
            x, y = hits[i]
            if grid[x][y] == 2:
                # add the hit back and union bricks around
                grid[x][y] = 1
                self.union_around(x, y, grid, uf)

            new_count = uf.counts[uf.find(m * n)]
            res[i] = max(new_count - count - 1, 0)
            count = new_count

        return res

    def union_around(self, i, j, grid, uf):
        m, n = len(grid), len(grid[0])
        p = i * n + j

        if i == 0:
            uf.union(m * n, p)

        for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                q = x * n + y
                uf.union(p, q)

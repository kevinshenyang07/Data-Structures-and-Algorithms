from union_find import UnionFind

# Number of Islands II
# A 2d grid map of m rows and n columns is initially filled with water.
# We may perform an addLand operation which turns the water at position (row, col) into a land.
# Given a list of positions to operate, count the number of islands after each addLand operation.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.
# Example:
# m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
# => [1, 1, 2, 3]
class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        uf = UnionFind(m * n)
        added = set()
        count = 0  # current number of islands
        res = []

        for i, j in positions:
            p = i * n + j
            added.add((i, j))
            count += 1

            for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and (x, y) in added:
                    q = x * n + y
                    # reduce count if two nodes are connected
                    # but currently in different trees
                    if uf.find(p) != uf.find(q):
                        count -= 1
                    uf.union(p, q)

            res.append(count)

        return res

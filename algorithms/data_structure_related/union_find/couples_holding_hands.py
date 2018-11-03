from union_find import UnionFind

# Couples Holding Hands
# think about each couple as a vertex in the graph, indexed from 0 to N - 1
# if there's a mismatch it must be cyclic: (0,2) - (2, 3) - (3, 1)
# for each cycle the minimum number of swaps is len(cycle) - 1
# which sum up to N - number of groups
class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        N = len(row) / 2
        uf = UnionFind(N)

        for i in range(N):
            x, y = row[2 * i], row[2 * i + 1]
            uf.union(x / 2, y / 2)

        return N - uf.num_groups

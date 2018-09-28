from union_find import UnionFind

# Friend Circles
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i + 1, n):
                if M[i][j] == 1:
                    uf.union(i, j)

        return uf.num_groups

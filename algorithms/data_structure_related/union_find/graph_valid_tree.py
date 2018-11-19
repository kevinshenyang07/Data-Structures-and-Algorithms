from union_find import UnionFind

# Graph Valid Tree
# given n nodes labeled from 0 to n-1 and a list of undirected edges
# write a function to check whether these edges make up a valid tree
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        uf = UnionFind(n)
        # no cycles
        for p, q in edges:
            if uf.find(p) == uf.find(q):
                return False
            uf.union(p, q)

        return uf.num_groups == 1

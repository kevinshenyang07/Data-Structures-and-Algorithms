from union_find import UnionFind

# Redundant Connection
# in this problem, a tree is an undirected graph that is connected and has no cycles
# the given input is a tree with N nodes (from 1 to N) but one additional edge added
# in each pair [u, v], u < v, and the edge is undirected
# return an edge that can be removed to make it tree again
# if there are multiple answers, return the answer that occurs last in the given input
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        uf = UnionFind(len(edges) + 1)

        for p, q in edges:
            if uf.find(p) == uf.find(q):
                return [p, q]
            uf.union(p, q)


# Redundant Connection II
# in this problem, a rooted tree is a directed graph such that, there is exactly one node (the root)
# for which all other nodes are descendants of this node, plus every node has exactly one parent,
# except for the root node which has no parents.
# given a graph started as a rooted tree, with one additional edge added
# each edge is a pair [u, v] taht means u is a parent of v
# return an edge that can be removed to make it a ROOTED tree again
# if there are multiple answers, return the answer that occurs last in the given input
class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        uf = UnionFind(len(edges) + 1)
        candidates = self.find_candidates(edges)
        # no nodes have two parents: fall back to Q1
        if not candidates:
            for p, q in edges:
                if uf.find(p) == uf.find(q):
                    return [p, q]
                uf.union(p, q)
        # remove the last edge that makes the graph a valid tree
        else:
            # union all edges except for the second candidate
            # if a cycle is found during the process
            # (not necessarily when the two nodes of first candidates are unioned)
            # the first candidate must be removed
            for p, q in edges:
                if p == candidates[1][0] and q == candidates[1][1]:
                    continue
                if uf.find(p) == uf.find(q):
                    return candidates[0]
                uf.union(p, q)
            return candidates[1]

    # find the two edges that two nodes share the same child
    def find_candidates(self, edges):
        parents = range(len(edges) + 1)
        for p, q in edges:
            # q is already a child of another node
            if parents[q] != q:
                return [[parents[q], q], [p, q]]
            parents[q] = p
        return []

# followup for Q2:
# what if the input is the root of a BST with a redundant edge?

from union_find import UnionFind

# Redundant Connection
# in this problem, a tree is an undirected graph that is connected and has no cycles
# the given input is a tree with N nodes (from 1 to N) but one additional edge added
# in each pair [u, v], u < v, and the edge is undirected
# return an edge that can be removed to make it tree again
# if there are multiple answers, return the answer that occurs last in the given input
class SolutionQ1(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        N = len(edges)
        uf = UnionFind(N + 1)

        for p, q in edges:
            if uf.find(p) == uf.find(q):
                return [p, q]
            uf.union(p, q)


# Redundant Connection II
# in this problem, a rooted tree is a directed graph such that, there is exactly one node (the root)
# for which all other nodes are descendants of this node, plus every node has exactly one parent,
# except for the root node which has no parents.
# each pair [u, v] means u is a parent of v
# return an edge that can be removed to make it a ROOTED tree again
# if there are multiple answers, return the answer that occurs last in the given input
class SolutionQ2(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        uf = UnionFind(len(edges) + 1)
        candidates = self.find_candidates(edges)  # edges that can be removed

        # no nodes have two parents: fall back to Q1
        if not candidates:
            for p, q in edges:
                if uf.find(p) == uf.find(q):
                    return [p, q]
                uf.union(p, q)
        # remove the last edge that makes the graph a valid tree
        else:
            for p, q in edges:
                u, v = candidates[1]
                # not using (remove) the last candidate edge
                if p == u and q == v:
                    continue
                # current edge has cycle
                if uf.find(p) == uf.find(q):
                    return candidates[0]
                uf.union(p, q)
            return candidates[1]

    # find the two edges that two nodes share the same child
    def find_candidates(self, edges):
        parents = range(len(edges) + 1)
        for p, q in edges:
            if parents[q] != q:  # q is already a child of another node
                return [[parents[q], q], [p, q]]
            parents[q] = p
        return []

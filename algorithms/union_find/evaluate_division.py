# Evaluate Division
class UnionFind(object):
    def __init__(self, n):
        self.parents = range(n)
        self.values = [1.0] * n  # initial value for each node

    # amortized O(1) time:
    def find(self, p):
        k = p
        while p != self.parents[p]:
            # path compression
            self.parents[p] = self.parents[self.parents[p]]
            p = self.parents[p]
        # the length of the previous path is now halfed
        return p

    # when merging tree b to tree a, calculate the adjustment multiple
    # by the ratio provided, then propagate it to every node in tree b
    # O(n) time because of that for loop
    def union(self, p, q, ratio):
        parent_p = self.find(p)
        parent_q = self.find(q)

        if parent_p == parent_q:  # p and q in one group
            return
        # p = 1, q = 2, ratio = 4 => x = 1 / (2 * 4)
        adj_mul = self.values[p] / (self.values[q] * ratio)
        for i in range(len(self.parents)):
            if self.parents[i] == parent_q:
                self.values[i] *= adj_mul
        # merge tree parent_q to tree parent_p
        self.parents[parent_q] = parent_p


class Solution(object):
    def calcEquation(self, equations, ratios, queries):
        """
        :type equations: List[List[str]]
        :type ratios: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        mapping = self.create_mapping(equations)
        uf = UnionFind(len(mapping))

        for i in range(len(equations)):
            a, b = equations[i]
            uf.union(mapping[a], mapping[b], ratios[i])

        res = []
        for a, b in queries:
            if a not in mapping or b not in mapping:
                res.append(-1.0)
            elif uf.find(mapping[a]) != uf.find(mapping[b]):
                res.append(-1.0)
            else:
                res.append(uf.values[mapping[a]] / uf.values[mapping[b]])

        return res

    def create_mapping(self, equations):
        mapping = {}  # str => id
        n = 0

        for i in range(len(equations)):
            a, b = equations[i]
            if a not in mapping:
                mapping[a] = n
                n += 1
            if b not in mapping:
                mapping[b] = n
                n += 1

        return mapping
# O(N * E + Q) time, O(N) space
# N being number of strings
# E being number of equations
# Q being number of queries

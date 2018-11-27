# Evaluate Division
class UnionFind(object):
    def __init__(self):
        self.parents = {}
        self.values = {}

    def find(self, p):
        # initialize
        if p not in self.parents:
            self.parents[p] = p
            self.values[p] = 1.0
        while p != self.parents[p]:
            # propagate the multiplier going up
            self.values[p] *= self.values[self.parents[p]]
            # path compression
            self.parents[p] = self.parents[self.parents[p]]
            p = self.parents[p]
        # the length of the previous path is now halfed
        return p

    def union(self, p, q, ratio):
        parent_p = self.find(p)
        parent_q = self.find(q)

        if parent_p == parent_q:  # p and q in one group
            return
        # calculate the adjustment multiplier
        # p = 1, q = 2, ratio = 4 => 1 / (2 * 4)
        # which will be propagated in find()
        self.values[parent_q] = self.values[p] / (self.values[q] * ratio)
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
        uf = UnionFind()
        for i in range(len(equations)):
            a, b = equations[i]
            uf.union(a, b, ratios[i])

        result = []
        for a, b in queries:
            if a not in uf.parents or b not in uf.parents:
                result.append(-1.0)
            elif uf.find(a) != uf.find(b):
                result.append(-1.0)
            else:
                result.append(uf.values[a] / uf.values[b])

        return result
# O(N * E + Q) time, O(N) space
# N being number of strings
# E being number of equations
# Q being number of queries

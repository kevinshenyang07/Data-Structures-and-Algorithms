from heapq import heappush, heappop
from collections import defaultdict


# Reconstruct Itinerary
# the tickets belong to a man who departs from JFK
# each ticket is an array of [from, to]
# get the itinerary with the smallest lexical ordering

# approach: dfs and build the Eulerian path backwards when the search returns
# assume there's at least one valid itinerary
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        res = []
        mapping = defaultdict(list)

        for dep, arr in tickets:
            heappush(mapping[dep], arr)

        self.dfs('JFK', mapping, res)
        return res

    def dfs(self, node, mapping, res):
        pq = mapping[node]
        while pq:
            self.dfs(res, mapping, heappop(pq))
        res.insert(0, node)
# O(n) time and space

from heapq import heappush, heappop

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
        mapping = {}

        for dep, arr in tickets:
            mapping[dep] = mapping.get(dep, [])
            mapping[arr] = mapping.get(arr, [])
            heappush(mapping[dep], arr)

        self.dfs(res, mapping, 'JFK')
        return res

    def dfs(self, res, mapping, node):
        pq = mapping[node]
        while pq:
            self.dfs(res, mapping, heappop(pq))
        res.insert(0, node)
# O(n) time and space

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
        self.result = []
        self.mapping = collections.defaultdict(list)

        for dep, arr in tickets:
            heappush(self.mapping[dep], arr)

        self.dfs('JFK')
        return self.result

    # a valid path must be a line with 0 or some cycles on certain nodes
    # => add none-cycle partial path to result first
    def dfs(self, dep):
        pq = self.mapping[dep]  # arrivals
        while pq:
            self.dfs(heappop(pq))
        self.result.insert(0, dep)
# O(n) time and space

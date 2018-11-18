from heapq import heappush, heappop

# Cheapest Flights Within K Stops
# There are n cities connected by m flights.
# Each fight starts from city u and arrives at v with a price w.
# Now given all the cities and flights, together with starting city src and the destination dst,
# your task is to find the cheapest price from src to dst with up to k stops.
# If there is no such route, output -1.
# Flights are directed, no duplicate flights or self-cycles.
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int

        !! K stops => K + 1 flights
        """
        graph = { i : {} for i in range(n) }
        for u, v, p in flights:
            graph[u][v] = p

        pq = [(0, src, K)]
        while pq:
            # Djikstra's algo that greedily look for closest next node
            cost, u, k = heappop(pq)
            if u == dst:
                return cost
            if k >= 0:
                for nbr in graph[u]:
                    new_cost = cost + graph[u][nbr]
                    heappush(pq, (new_cost, nbr, k - 1))
        return -1
# O(m + nlogn) time, O(n) time

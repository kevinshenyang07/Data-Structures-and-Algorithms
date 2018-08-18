from collections import defaultdict


# Network Delay Time
# There are N network nodes, labelled 1 to N. Given times, a list of travel times as directed edges times[i] = (u, v, w),
# where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.
# Now send a signal from node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.
class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        adj_map = defaultdict(dict)
        dist = { i: 2 ** 31 - 1 for i in range(1, N + 1) }
        dist[K] = 0  # make sure BFS starts with K

        for u, v, w in times:
            adj_map[u][v] = w

        # queue or heap not compatible with this algo
        # because after (d, v) is enqueued dist[v] could change
        nodes = set(range(1, N + 1))
        while nodes:
            # u to be the node with smallest dist[u]
            u = None
            for node in nodes:
                if not u or dist[node] < dist[u]:
                    u = node
            nodes.remove(u)

            # update shortest path dist of adj nodes
            for v in adj_map[u]:
                dist[v] = min(dist[v], dist[u] + adj_map[u][v])

        max_dist = max(dist.values())
        return max_dist if max_dist < 2 ** 31 - 1 else - 1

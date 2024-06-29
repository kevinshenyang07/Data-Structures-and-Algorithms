# Network Delay Time
# There are N network nodes, labelled 1 to N. Given times, a list of travel times as directed edges times[i] = (u, v, w),
# where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.
# Now send a signal from node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        minTime = [float('inf')] * (n + 1)  # sys.maxsize does not work on mac. 
        minTime[k] = 0
        dist = {}
        for i, j, d in times:
            if i not in dist:
                dist[i] = {}
            dist[i][j] = d
        
        queue = collections.deque([k])
        while queue:
            i = queue.popleft()
            if i not in dist:
                continue
            for j, d in dist[i].items():
                # Shouldn't visit each node exactly once - if distance to that
                # node reduces, its child nodes should be updated.
                if (minTime[j] > minTime[i] + d):
                    minTime[j] = minTime[i] + d
                    queue.append(j)
        maxTime = float('-inf')
        for i in range(1, n + 1):
            maxTime = max(maxTime, minTime[i])
        return maxTime if maxTime != float('inf') else -1

from heapq import heappush, heappop

# The Skyline Problem
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(buildings) == 0:
            return []
        # goals when 2+ events happen at the same position:
        # 1. starting events should always be processed earlier than ending events
        # 2. starting events with larget heights should be processed first
        # 3. events with the same height as the last critical point should be skipped
        event_set = set()
        for L, R, H in buildings:
            event_set.add((L, H, R))  # need to know where the height 'expire'
            event_set.add((R, 0, 0))  # set H and R as 0 for goal 1
        events = sorted(event_set, key = lambda t: (t[0], -t[1], t[2]))

        # (-height, ending position), with initial element to be a horizon that never 'expire'
        pq = [(0, float('inf'))]
        res = []

        for x, H, R in events:
            # remove 'expired' heights
            while x >= pq[0][1]:
                heapq.heappop(pq)
            # add height for a starting event
            # a smaller height added later won't change max height
            if R > 0:
                heapq.heappush(pq, (-H, R))
            # add the new critical point if max height changes (goal 3)
            max_H = -pq[0][0]
            if not res or res[-1][1] != max_H:
                res.append([x, max_H])

        return res

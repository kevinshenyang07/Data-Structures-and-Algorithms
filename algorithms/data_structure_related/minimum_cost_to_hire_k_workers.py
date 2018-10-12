from heapq import heappush, heappop

# Minimum Cost to Hire K Workers
# base case:
# for a group of exactly k workers, to satisfy every one
# the minmal cost = highest ratio of wage to quality * total quality
# extension:
# sort the ratio from low to high
# then in window [0 i], only the last (and highest) ratio can satisfy any k workers in the range
# then the cost can be minimized by finding the lowest total quality
class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        n = len(quality)
        workers = sorted((float(wage[i]) / quality[i], quality[i]) for i in range(n))

        heap = []
        qsum = 0  # sum of quality of the k workers picked
        res = float('inf')

        for i in range(n):
            r, q = workers[i]
            heapq.heappush(heap, -q)
            qsum += q

            if len(heap) > K:
                # drop the worker with highest quality to minize cost
                qsum += heapq.heappop(heap)  # qsum -= q
            if len(heap) == K:
                res = min(res, qsum * r)

        return res
# O(nlogn) time, O(n) space

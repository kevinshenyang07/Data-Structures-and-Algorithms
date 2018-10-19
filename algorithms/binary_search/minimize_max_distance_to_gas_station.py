import math

# Minimize Max Distance to Gas Station
# On a horizontal number line, we have gas stations at positions stations[0],
# stations[1], ..., stations[N-1], where N = stations.length.
# Now, we add K more gas stations so that D, the maximum distance between adjacent gas stations, is minimized.
# Return the smallest possible value of D.
# Note:
# 1. 10 <= stations.length <= 2000, stations[i] will be an integer
# 2. 1 <= K <= 1e6
# 3. answers within 10^-6 of the true value will be accepted as correct
#
# Intuition:
# with K gas stations, can we make every adjacent distance between gas stations at most D?
# Specific:
# with D' being a possible answer, for each interval with W = stations[i+1] - stations[i]
# W / D' stations are needed to ensure every subinterval has size less than D‘
class Solution(object):
    def minmaxGasDist(self, stations, K):
        """
        :type stations: List[int]
        :type K: int
        :rtype: float
        """
        # lower / upper bound of the answer, upper bound does not really matter
        lo, hi = 0, stations[-1] - stations[0]
        delta = 1e-6
        # search interval
        while lo + delta < hi:
            mid = lo + (hi - lo) / 2.0

            cnt = 0  # the number of gas station we need to make it possible
            for i in range(len(stations) - 1):
                cnt += int((stations[i + 1] - stations[i]) / mid)

            if cnt <= K:  # mid is too small to realize using only K more stations
                hi = mid
            else:  # mid is possible and we can continue to find a bigger one
                lo = mid

        return lo
# O(nlogw) time, w being the range of possible answer / delta

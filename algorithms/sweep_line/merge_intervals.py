# Merge Intervals
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key = lambda interval: interval.start)
        merged = []

        # list out three situations:
        # 1. merged is empty => append interval
        # 2. last.end < inter.start => append interval
        # 3. last.end >= inter.start => update last.end
        for interval in intervals:
            if merged and merged[-1].end >= interval.start:
                merged[-1].end = max(merged[-1].end, interval.end)
            else:
                merged.append(interval)

        return merged

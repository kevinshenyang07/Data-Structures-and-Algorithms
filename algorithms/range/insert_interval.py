# Insert Interval
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            return [newInterval]

        res = []
        for i, interval in enumerate(intervals):
            # newInterval is after current interval and not overlapping
            if interval.end < newInterval.start:
                res.append(interval)
            # newInterval is before current interval and not overlapping
            elif interval.start > newInterval.end:
                return res + [newInterval] + intervals[i:]
            # newInterval overlaps with current interval
            else:
                newInterval.start = min(newInterval.start, interval.start)
                newInterval.end = max(newInterval.end, interval.end)

        res.append(newInterval)
        return res

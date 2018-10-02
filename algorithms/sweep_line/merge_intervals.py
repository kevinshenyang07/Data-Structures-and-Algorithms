# Merge Intervals
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class SolutionV1(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda inter: inter.start)
        merged = []

        # list out three situations:
        # 1. merged is empty => append interval
        # 2. last.end < inter.start => append interval
        # 3. last.end >= inter.start => update last.end
        for inter in intervals:
            if merged and merged[-1].end >= inter.start:
                merged[-1].end = max(merged[-1].end, inter.end)
            else:
                merged.append(inter)

        return merged

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


# Merge Intervals
def merge_intervals(intervals):
    # not sweep line approach
    if len(intervals) <= 1:
        return intervals
    intervals.sort(key=lambda inter: inter.start)
    merged = []
    for inter in intervals:
        # list out three situations:
        # 1. merged is empty => append interval
        # 2. merged is not empty, last.end < inter.start => append interval
        # 3. merged is not empty, last.end >= inter.start => update last.end
        if merged and merged[-1].end >= inter.start:
            merged[-1].end = max(merged[-1].end, inter.end)
        else:
            merged.append(inter)
    return merged


# Meeting Rooms II
# given an array of intervals, find the minimum number of conference rooms required
def min_meeting_rooms(intervals):
    """
    :type intervals: List[Interval]
    :rtype: int
    """
    points = []
    for interval in intervals:
        points.append((interval.start, 1))
        points.append((interval.end, -1))
    points.sort()

    num_rooms = max_num_rooms = 0
    for t, dt in points:
        num_rooms += dt
        max_num_rooms = max(max_num_rooms, num_rooms)

    return max_num_rooms

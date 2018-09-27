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
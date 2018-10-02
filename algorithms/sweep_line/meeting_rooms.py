# Meeting Rooms II
# given an array of intervals, find the minimum number of conference rooms required
class Solution(object):
    def minMeetingRooms(intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        events = []
        for interval in intervals:
            events.append((interval.start, 1))
            events.append((interval.end, -1))
        events.sort()

        num_rooms = max_num_rooms = 0
        for t, dt in events:
            num_rooms += dt
            max_num_rooms = max(max_num_rooms, num_rooms)

        return max_num_rooms

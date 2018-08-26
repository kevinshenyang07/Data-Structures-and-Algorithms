# Employee Free Time
# We are given a list schedule of employees, which represents the working time for each employee.
# Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.
# Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.
# Example: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
#                  => [[5,6],[7,9]]
# Note: schedule and schedule[i] are lists with lengths in range [1, 50], start is always smaller than end
class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        # generator expression must be parenthesized if not sole argument
        intervals = sorted((i for emp in schedule for i in emp), key=lambda i: i.start)
        free_time = []
        curr_end = intervals[0].end

        for i in range(1, len(intervals)):
            interval = intervals[i]
            if curr_end < interval.start:
                free_time.append(Interval(curr_end, interval.start))
            curr_end = max(curr_end, interval.end)

        return free_time
# O(nlogn) time, O(n) space
# can be reduced to O(nlogk) time using approach of merge k sorted lists

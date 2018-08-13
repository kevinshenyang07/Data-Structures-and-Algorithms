# Next Closest Time
# Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits.
# There is no limit on how many times a digit can be reused.
# Assume the given input string is always valid
# f("23:59") => f("22:22")
class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        nums = set()
        for i in range(len(time)):
            if i != 2:
                nums.add(time[i])

        new_times = []
        for H1 in nums:
            for H2 in nums:
                for M1 in nums:
                    for M2 in nums:
                        new_time = H1 + H2 + ':' + M1 + M2
                        if 0 <= int(new_time[:2]) < 24 and 0 <= int(new_time[3:]) < 60:
                            new_times.append(new_time)

        min_diff = 2 ** 31 - 1
        min_time = time

        for new_time in new_times:
            curr_diff = self.diff(time, new_time)
            if time != new_time and curr_diff < min_diff:
                min_time = new_time
                min_diff = curr_diff

        return min_time

    def diff(self, t1, t2):
        h1, m1 = int(t1[:2]), int(t1[3:])
        h2, m2 = int(t2[:2]), int(t2[3:])

        if t1 > t2:
            return (24 - h1) * 60 + m1 + h2 * 60 + m2
        else:
            return (h2 - h1) * 60 + m2 - m1

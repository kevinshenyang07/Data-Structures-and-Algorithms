# Circular Array Loop
# A loop starts and ends at a particular index with more than 1 element along the loop.
# The loop must be "forward" or "backward'. Assume no zeros in the array.
# similar to find circle in linked list
class Solution(object):
    def circularArrayLoop(self, steps):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(steps)):
            if steps[i] == 0:
                continue

            slow = fast = i
            while slow >= 0 and fast >= 0:
                slow = self.next(steps, slow)
                fast = self.next(steps, self.next(steps, fast))
                if slow >= 0 and slow == fast:
                    return True

            slow = i
            while slow >= 0 and steps[i] * steps[slow] > 0:
                next_slow = self.next(steps, slow)
                steps[slow] = 0
                slow = next_slow

        return False

    def next(self, steps, i):
        if i < 0:  # case when the fast pointer has reached an invalid state
            return -1

        n = len(steps)
        next_i = (i + steps[i] + n) % n  # both pos and neg situations

        if steps[i] * steps[next_i] < 0:  # different directions
            return -1
        if i == next_i:  # self loop
            return -1

        return next_i
# O(n) time, O(1) space

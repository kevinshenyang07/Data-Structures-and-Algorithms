# Longest Mountain in Array
# two pass O(n) space version: keep track of upward / downward length until A[i]
class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        up = down = 0  # count of continuous upward / downward trends between A[i - 1] and A[i]
        res = 0

        for i in range(1, len(A)):
            # goes from down to up or flat
            if (down > 0 and A[i - 1] < A[i]) or A[i - 1] == A[i]:
                up = down = 0
            if A[i - 1] < A[i]:
                up += 1
            if A[i - 1] > A[i]:
                down += 1
            if up > 0 and down > 0:
                res = max(res, up + down + 1)

        return res
# O(n) time, O(1) space
# followup:
# if a mountain can have multiple ups and downs, as long as the leftmost / rightmost points
# are the lowest, what would be the new answer?

# Max Consecutive Ones II
# An array only contains 0 and 1.
# Find the maximum number of consecutive 1s in the array if you can flip at most one 0.
# f([1,0,1,1,0]) => 4
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # maintain a window of previous ones, zeros in the middle and current ones
        prev_ones = zeros = curr_ones = 0
        max_consec = 0

        for num in nums:
            if num == 1:
                if zeros == 0:
                    prev_ones += 1
                else:
                    curr_ones += 1
            else:
                if curr_ones == 0:
                    zeros += 1
                else:  # next sequence of zeros found
                    if zeros > 1:
                        max_consec = max(max_consec, 1 + curr_ones)
                    else:
                        max_consec = max(max_consec, prev_ones + zeros + curr_ones)
                    prev_ones = curr_ones
                    curr_ones = 0
                    zeros = 1

        if zeros > 1:
            max_consec = max(max_consec, 1 + curr_ones)
        else:
            # + zeros for case like [1]
            max_consec = max(max_consec, prev_ones + zeros + curr_ones)

        return max_consec
# O(n) time, O(1) space, also work for inifite stream
# followup: what if you can flip at most k 0s?

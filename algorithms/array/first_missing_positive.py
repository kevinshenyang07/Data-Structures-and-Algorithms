# First Missing Positive
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # let the length of original array to be L, the first missing positive
        # must be in range [1, L+1] => add 0 for padding
        nums.append(0)
        n = len(nums)
        # remove numbers that cannot be the answer (out of range of [1, L])
        for i, num in enumerate(nums):
            if num < 0 or num >= n:
                nums[i] = 0
        # use the index as the hash to record the frequency of each number
        for i, num in enumerate(nums):
            nums[num % n] += n
        # nums[i] = its original value + number of occurrences of i in the array * n
        for i in range(1, n):
            if nums[i] / n == 0:
                return i

        return n
# O(n) time, O(1) space
# test cases:
# [0,3] => 1
# [1,2] => 3
# [7,8,9,11,12] => 1

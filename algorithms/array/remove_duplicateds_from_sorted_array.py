# Remove Duplicates from Sorted Array II
# Given a sorted array nums, remove the duplicates in-place such that
# duplicates appeared at most twice and return the new length.
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0  # next index to move curr number to
        for num in nums:
            # nums[i - 2] == num - 2: no duplicates
            # nums[i - 2] == num - 1: repeated twice
            if i < 2 or num > nums[i - 2]:
                nums[i] = num
                i += 1
        return i
# [1, 1, 1, 2, 2, 3] => 5
# [0, 0, 1, 1, 1, 1, 2, 3, 3] => 7

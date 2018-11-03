# Wiggle Sort
# reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]...
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        # greedy
        for i in range(1, len(nums)):
            # when i is odd, nums[i-2] >= nums[i-1] <= nums[i]
            if i % 2 == 1 and nums[i-1] > nums[i]:
                # nums[i-2] still greater than nums[i]
                nums[i-1], nums[i] = nums[i], nums[i-1]
            # when i is even, nums[i-2] <= nums[i-1] >= nums[i]
            if i % 2 != 1 and nums[i-1] < nums[i]:
                # nums[i-2] still greater
                nums[i-1], nums[i] = nums[i], nums[i-1]

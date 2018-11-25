# Find Peak Element
# A peak element is an element that is greater than its neighbors.
# Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
# You may imagine that nums[-1] = nums[n] = -∞.
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return -1

        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) / 2

            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            # for cases when nums[mid - 1] > nums[mid] < nums[mid + 1],
            # either left or right has an answer
            if nums[mid - 1] < nums[mid] < nums[mid + 1]:
                left = mid
            else:
                right = mid

        if nums[left] < nums[right]:
            return right
        else:
            return left

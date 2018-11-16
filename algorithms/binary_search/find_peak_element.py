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

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2

            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid - 1] < nums[mid] < nums[mid + 1]:
                # there must be a peak between [mid+1, -1] because
                # if nums[mid + 1] > nums[mid + 2]: return mid + 1
                # else nums[mid + 1] < nums[mid + 2]: repeat previous process
                start = mid
            else:
                # vice versa
                end = mid

        if nums[start] >= nums[end]:
            return start
        else:
            return end

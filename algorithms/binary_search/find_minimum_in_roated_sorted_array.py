# Find Minimum in Rotated Sorted Array II
# The array may contain duplicates.
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left + 1 < right:
            mid = left + (right - left) / 2

            if nums[mid] < nums[right]:  # case 1 and 2
                right = mid
            elif nums[mid] > nums[right]:  # case 3
                left = mid
            else:  # values are the same from mid to right
                right -= 1  # look left to see if it equals to nums[mid]

        if nums[left] < nums[right]:
            return nums[left]
        else:
            return nums[right]
# three cases:
# 1. not rotated
# 2. rotated, left part steeper than right part
# 3. rotated, right part steeper than left part
# actions:
# 1. nums[left] < nums[mid] < nums[right] => take left
# 2. nums[mid] < nums[left] and nums[mid] < nums[right] => take left
# 3. nums[mid] > nums[left] and nums[mid] > nums[right] => take right

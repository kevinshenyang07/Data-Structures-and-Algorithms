# Single Element in a Sorted Array
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left < right:
            # get the first element of the middle pair
            # which should be at an even index if the left part is sorted
            # Example:
            # Index: 0 1 2 3 4 5 6
            # Array: 1 1 3 3 4 8 8
            #            ^
            mid = left + (right - left) / 2
            if mid % 2 == 1:
                mid -= 1
            # didn't find a pair, the single element must be on the left
            # (pipes mean left & right)
            # Example: |0 1 1 3 3 6 6|
            #               ^ ^
            # Next:    |0 1 1|3 3 6 6
            if nums[mid] != nums[mid + 1]:
                right = mid
            # found a pair, the single element must be on the right
            # Example: |1 1 3 3 5 6 6|
            #               ^ ^
            # Next:     1 1 3 3|5 6 6|
            else:
                left = mid + 2
        # left should always be at the beginning of a pair
        # When left > right, left must be the single element
        return nums[left]

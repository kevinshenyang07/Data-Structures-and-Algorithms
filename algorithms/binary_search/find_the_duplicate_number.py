# Find the Duplicate Number
# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
# find the duplicate one.
# There is only one duplicate number, but it can be repeated multiple times.
# Note: You cannot modify the array, no extra space is allowed.
class SolutionV1(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo, hi = 1, len(nums) - 1

        while lo < hi:
            mid = lo + (hi - lo) / 2

            count = 0
            for num in nums:
                if num <= mid:
                    count += 1

            if count <= mid:
                lo = mid + 1
            else:
                hi = mid

        return lo
# O(nlogn) time, O(1) space


# if the array can be modified:
class SolutionV2(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            n = abs(nums[i])
            # imagine a sorted array from 0 - n
            # n should be at index n in that array
            if nums[n] > 0:
                nums[n] *= -1
            # if n has already been marked
            else:
                return n
        return -1
# O(n) time, O(1) space

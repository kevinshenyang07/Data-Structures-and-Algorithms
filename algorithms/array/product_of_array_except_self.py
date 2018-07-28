# Product of Array Except Self
# f([1,2,3,4]) => [24,12,8,6]
# solve it without division and in O(n) time and O(1) extra space
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []

        res = [0] * len(nums)

        res[0] = 1
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]  # product of previous numbers

        right = 1  # product of numbers from index i to n - 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res

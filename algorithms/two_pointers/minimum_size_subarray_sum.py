# Minimum Size Subarray Sum
# Given an array of n positive integers and a positive integer s,
# find the minimal length of a contiguous subarray of which the sum ≥ s.
# If there isn't one, return 0 instead.

# sliding window version
class Solution(object):
    def minSubArrayLen(self, s, nums):
        if not nums:
            return 0
        # initial window
        i = j = 0
        subtotal = nums[0]
        min_len = float('inf')

        while j < len(nums):
            if subtotal >= s:
                min_len = min(min_len, j - i + 1)
                subtotal -= nums[i]
                i += 1
            else:
                j += 1
                if j < len(nums):
                    subtotal += nums[j]

        return min_len if min_len < float('inf') else 0
# O(n) time, O(1) space


# followup to provide another version: prefix sum + binary search
class Solution(object):
    def minSubArrayLen(self, s, nums):
        if not nums:
            return 0
        # since prefix sum is ascending, it can be used to find
        # the smallest window from index i with range sum >= s
        pre_sum = [0] * len(nums)
        pre_sum[0] = nums[0]
        for i in range(1, len(nums)):
            pre_sum[i] = pre_sum[i - 1] + nums[i]

        min_len = float('inf')
        for i in range(len(nums)):
            curr_min_len = self.smallest_window(s, pre_sum, i)
            min_len = min(min_len, curr_min_len)

        return min_len if min_len < float('inf') else 0

    def smallest_window(self, s, pre_sum, i):
        left, right = i, len(pre_sum) - 1
        # important! handle the case when querying range from 0
        offset = 0 if i == 0 else pre_sum[i - 1]

        while left + 1 < right:
            mid = left + (right - left) / 2
            subtotal = pre_sum[mid] - offset
            if subtotal < s:
                left = mid
            elif subtotal > s:
                right = mid
            else:
                return mid - i + 1

        if pre_sum[left] - offset >= s:
            return left - i + 1
        if pre_sum[right] - offset >= s:
            return right - i + 1
        return float('inf')
# O(nlogn) time, O(n) space

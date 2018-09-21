# Maximum Sum of 3 Non-Overlapping Subarrays
# In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.
# Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.
# Return the result as a list of indices representing the starting position of each interval (0-indexed).
# If there are multiple answers, return the lexicographically smallest one.
# Assume k is always valid
# f([1,2,1,2,6,7,5,1], 2) => [0, 3, 5]
class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        pos_before[i]: within range of [0, i], the index x that maximize sum(nums[x:x+k])
        pos_after[i]: within range of [i, n), the index x that maximize sum(nums[x:x+k])
        sums[i]: sum(nums[i:i+k])
        """
        n = len(nums)
        pos_before = [0] * n
        pos_after = [n - k] * n
        sums = []

        # dp on pos_before
        # calculate sums at the same time
        curr_sum = max_sum = sum(nums[:k])
        sums.append(curr_sum)
        for i in range(k, n):
            curr_sum += nums[i] - nums[i - k]
            sums.append(curr_sum)

            if curr_sum > max_sum:
                pos_before[i] = i - k + 1
                max_sum = curr_sum
            else:
                pos_before[i] = pos_before[i - 1]

        # dp on pos_after
        curr_sum = max_sum = sum(nums[n-k:])
        for i in range(n - k - 1, -1, -1):
            curr_sum += nums[i] - nums[i + k]

            if curr_sum > max_sum:
                pos_after[i] = i
                max_sum = curr_sum
            else:
                pos_after[i] = pos_after[i + 1]

        # iterate possible indices of the subarray in the middle
        max_sum = 0
        res = []
        for i in range(k, n - k * 2 + 1):
            l = pos_before[i - 1]
            r = pos_after[i + k]

            curr_three_sum = sums[l] + sums[i] + sums[r]

            if curr_three_sum > max_sum:
                max_sum = curr_three_sum
                res = [l, i, r]

        return res

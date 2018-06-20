# Continuous Subarray Sum
# given a list of non-negative numbers and a target integer k, write a function to check
# if the array has a continuous subarray of size at least 2 that sums up to the multiple of k
class Solution(object):
    # suboptimal approach: prefix_sum with O(n^2) time
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return False
        if k == 0:
            for i in range(len(nums) - 1):
                if nums[i] + nums[i+1] == 0:
                    return True
            return False

        k = abs(k)
        # keep track of the smallest index for each mod result
        # initial value for case when (nums[0] + nums[1]) % k == 0
        mods = { 0: -1 }
        cum_sum_mod_k = 0

        for i, num in enumerate(nums):
            cum_sum_mod_k = (cum_sum_mod_k + num) % k
            if cum_sum_mod_k not in mods:
                mods[cum_sum_mod_k] = i
            elif i - mods[mod] >= 2:
                # nums[mods[cum_sum_mod_k]+1:i+1] mush be a multiple of k
                return True

        return False
# O(n) time, O(k) space

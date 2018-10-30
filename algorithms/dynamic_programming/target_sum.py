# Target Sum
# The original problem statement is equivalent to:
# Find a subset of nums that need to be positive, and the rest of them negative, such that the sum is equal to target.
# Let P be the positive subset and N be the negative subset, then we have:
# sum(P) - sum(N) = target
# => 2 * sum(P) = target + sum(P) + sum(N)
# => sum(P) = (target + sum(nums)) / 2  (which alos implies that target + sum(nums) must be even)
# => the problem becomes finding subsets that each sum up to target
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        total = sum(nums)

        if total < target or (target + total) % 2 == 1:
            return 0

        return self.subset_sum_ways(nums, (target + total) / 2)

    def subset_sum_ways(self, nums, subtotal):
        """
        dp[i]: ways to pick a subset of nums that sum up to i (target)
        dp[i] = dp[i - nums[0]] + ... + dp[i - nums[-1]]
        """
        dp = [0] * (subtotal + 1)
        dp[0] = 1  # one way to pick nothing

        # use numbers from 0 to index of current num
        for num in nums:
            # to avoid num being used twice
            for i in range(subtotal, num - 1, -1):
                dp[i] += dp[i - num]

        return dp[-1]
# self.subset_sum_ways([1,2,3,4], 4)
#
# 1 7 [1, 0, 0, 0, 0, 0, 0, 0]
# 1 6 [1, 0, 0, 0, 0, 0, 0, 0]
# 1 5 [1, 0, 0, 0, 0, 0, 0, 0]
# 1 4 [1, 0, 0, 0, 0, 0, 0, 0]
# 1 3 [1, 0, 0, 0, 0, 0, 0, 0]
# 1 2 [1, 0, 0, 0, 0, 0, 0, 0]
# 1 1 [1, 1, 0, 0, 0, 0, 0, 0]
#
# 2 7 [1, 1, 0, 0, 0, 0, 0, 0]
# 2 6 [1, 1, 0, 0, 0, 0, 0, 0]
# 2 5 [1, 1, 0, 0, 0, 0, 0, 0]
# 2 4 [1, 1, 0, 0, 0, 0, 0, 0]
# 2 3 [1, 1, 0, 1, 0, 0, 0, 0]
# 2 2 [1, 1, 1, 1, 0, 0, 0, 0]
#
# 3 7 [1, 1, 1, 1, 0, 0, 0, 0]
# 3 6 [1, 1, 1, 1, 0, 0, 1, 0]
# 3 5 [1, 1, 1, 1, 0, 1, 1, 0]
# 3 4 [1, 1, 1, 1, 1, 1, 1, 0]
# 3 3 [1, 1, 1, 2, 1, 1, 1, 0]
#
# 4 7 [1, 1, 1, 2, 1, 1, 1, 2]
# 4 6 [1, 1, 1, 2, 1, 1, 2, 2]
# 4 5 [1, 1, 1, 2, 1, 2, 2, 2]
# 4 4 [1, 1, 1, 2, 2, 2, 2, 2]

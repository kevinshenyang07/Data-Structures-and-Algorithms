# House Robber II
# all houses are arranged in a circle
class SolutionQ2(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return nums[0]

        return max(self.rob_from(nums, 0, len(nums) - 1), self.rob_from(nums, 1, len(nums)))

    def rob_from(self, nums, i, j):
        rob_curr = skip_curr = 0

        for k in range(i, j):
            rob_prev, skip_prev = rob_curr, skip_curr

            rob_curr = skip_prev + nums[k]
            skip_curr = max(skip_curr, rob_prev)

        return max(rob_curr, skip_curr)

# to make sure the first or the last house is not robbed, simply exclude it
#    [5, 2, 3, 4]

#    [5, 2, 3]
# [0, 5, 2, 8] R
# [0, 0, 5, 5] N

#       [2, 3, 4]
#    [0, 2, 3, 6] R
#    [0, 0, 2, 3] N

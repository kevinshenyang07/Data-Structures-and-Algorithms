# Partition to K Equal Sum Subsets
# for each bucket, try all possible content O(k*2^n) -- no good
# for each item, try all possible destined bucket O(n^k) -- doable
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        self.sums = [0] * k  # sum by partition
        self.target = sum(nums) / k
        # start with bigger nums to stop early
        nums.sort(key=lambda x: -x)

        return self.dfs(0, nums)

    def dfs(self, i, nums):
        sums = self.sums

        if i == len(nums):
            return True

        for j in range(len(sums)):  # range(k)
            sums[j] += nums[i]  # add nums[i] to partition j
            # has valid partitioning
            if sums[j] <= self.target and self.dfs(i + 1, nums):
                return True
            else:
                sums[j] -= nums[i]  # take nums[i] out
                # no numbers can form a valid partition j
                if sums[j] == 0:
                    break
        return False

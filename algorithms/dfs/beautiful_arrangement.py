# Beautiful Arrangement
class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        nums = range(1, N + 1)
        return self.helper(nums, N)

    def helper(self, nums, n):
        if n == 0: return 1

        cnt = 0
        # generate permutations by swapping elements
        for i in range(n):
            if n % nums[i] == 0 or nums[i] % n == 0:
                # swap one valid number to position n (index n - 1)
                self.swap(nums, i, n - 1)
                cnt += self.helper(nums, n - 1)
                self.swap(nums, i, n - 1)
        return cnt

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
# O(k) time, O(n) space, k being number of valid permutations

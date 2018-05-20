# one-pass, in-place
class Solution(object):
    def sort_colors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # [i, j) is color 0, [j, k) is unknown, [k, len(nums)-1) is color 2
        i, j, k = 0, 0, len(nums) - 1

        while j <= k:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] == 1:
                j += 1
            else:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
# O(n) time, O(1) space
# find element a, b, c that sum to 0, return unique combinations
def three_sum(nums):
    result = []
    nums.sort()
    for i in range(len(nums) - 2):
        # if a number is already tested, move to the next one
        if i > 0 and nums[i-1] == nums[i]:
            continue
        # find possible combinations on the right
        l, r = i + 1, len(nums) - 1
        while l < r:
            sum_of_three = nums[i] + nums[l] + nums[r]
            if sum_of_three < 0:
                l += 1
            elif sum_of_three > 0:
                r -= 1
            else:
                result.append([nums[i], nums[l], nums[r]])
                # skip the duplicates
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r-1] == nums[r]:
                    r -= 1
                l += 1; r -= 1
    return result
# O(n^2) time, O(1) space


# 3Sum Smaller
# Given an array of n integers nums and a target, find the number of index triplets i, j, k
# with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.
# f([-2,0,1,3], 2) => 2
class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count = 0
        nums.sort()

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] < target:
                    # add count by 1 for each nums[i] + nums[left] + nums[j]
                    # while j is in range [left + 1, right]
                    count += right -left
                    left += 1
                else:
                    right -= 1

        return count
# O(n^2) time, O(1) space

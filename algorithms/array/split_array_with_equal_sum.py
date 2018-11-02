# Split Array with Equal Sum
# Given an array with n integers, you need to find if there are index triplets (i, j, k) which satisfies following conditions:
# 0 < i, i + 1 < j, j + 1 < k < n - 1
# Sum of subarrays from (0, i - 1), (i + 1, j - 1), (j + 1, k - 1) and (k + 1, n - 1) should be equal.
# f([1,2,1,2,1,2,1]) => true

# => find i, j, k that:
# => sum(arr[:i]) == sum(arr[i+1:j]) == sum(arr[j+1:k]) == sum(arr[k+1:])
# => pre_sum[i - 1] == pre_sum[j - 1] - pre_sum[i]
#                      == pre_sum[k - 1] - pre_sum[j]
#                      == pre_sum[n - 1] - pre_sum[k]
class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 6:
            return False

        n = len(nums)
        pre_sum = [0] * len(nums)
        pre_sum[0] = nums[0]
        for i in range(1, n):
            pre_sum[i] = pre_sum[i - 1] + nums[i]

        # use j to divide into 2 * 2 ranges
        for j in range(3, n - 3):
            values = set()  # values that possibly satisfy the multi-equaliy

            for i in range(1, j - 1):
                if pre_sum[i - 1] == pre_sum[j - 1] - pre_sum[i]:
                    values.add(pre_sum[i - 1])

            for k in range(j + 2, n - 1):
                sum_after_k = pre_sum[n - 1] - pre_sum[k]
                if sum_after_k in values and sum_after_k == pre_sum[k - 1] - pre_sum[j]:
                    return True

        return False
# O(n ^ 2) time, O(n) space

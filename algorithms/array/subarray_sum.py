# Subarray Sum Equals K
def subarray_sum_optimized(nums, k):
    subtotal = ans = 0
    counter = { 0: 1 }
    # let current index to be i
    # key: an element in prefix_sum built so far
    # val: numbers of indices j that satifies k = prefix_sum[i+1] - prefix_sum[j], while j < i
    # e.g. if prefix_sum[i+1] = 5, k = 2, then any j that makes prefix_sum[j] == 5 - 2
    #      will make nums[j:i+1] add up to k, since k = prefix_sum[i+1] - prefix_sum[j]

    for num in nums:
        subtotal += num  # prefix_sum[i]

        if subtotal - k in counter:
            ans += counter[subtotal - k]

        counter[subtotal] = counter.get(subtotal, 0) + 1

    return ans
# O(n) time and space


# Continuous Subarray Sum
# given a list of non-negative numbers and a target integer k, write a function to check
# if the array has a continuous subarray of size at least 2 that sums up to the multiple of k
def check_subarray_sum(nums, k):
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
        elif i - mods[cum_sum_mod_k] >= 2:
            # nums[mods[cum_sum_mod_k]+1:i+1] mush be a multiple of k
            return True

    return False
# O(n) time, O(k) space


# Maximum Size Subarray Sum Equals k
# Given an array nums and a target value k, find the maximum length of a subarray that sums to k.
# f([1, -1, 5, -2, 3], 3) => 4
# valid subarray is: [1, -1, 5, -2]
def max_subarray_size(nums, k):
    max_size, acc = 0, 0  # answer and the accumulative value of nums
    mp = { 0: -1 }  # key is acc value, and value is the index

    for i in xrange(len(nums)):
        acc += nums[i]
        if acc not in mp:
            mp[acc] = i
        if acc - k in mp:
            max_size = max(max_size, i - mp[acc - k])
    return max_size
# O(n) time and space

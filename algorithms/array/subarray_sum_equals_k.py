# Subarray Sum Equals K
def subarray_sum(nums, k):
    prefix_sum = [0] * (len(nums) + 1)  # plue one length to deal with i = 0
    for i in range(nums):
        prefix_sum[i+1] = prefix_sum[i] + nums[i]
        # => sum(nums[i:j+1]) == prefix_sum[j+1] - prefix_sum[i]
    ans = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
           # key to this problem
           if prefix_sum[j+1] - prefix_sum[i] == k:
               ans += 1
    return ans
# O(n^2) time and space for prefix sum
# O(n^3) time and O(1) space for brute force


def subarray_sum_optimized(nums, k):
    subtotal = ans = 0
    counter = { 0: 1 }
    # image current index is i
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

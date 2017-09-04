# Two Sum - Sorted Array
def two_sum2(nums, target):
    start, end = 0, len(nums) - 1
    while start < end:
        if nums[start] + nums[end] == target:
            return [start + 1, end + 1]
        elif nums[start] + nums[end] < target:
            start += 1
        else:
            end -= 1
    return []
# O(n) time, O(1) space


# Two Sum - Closet to Target

# Two Sum - Difference Equals to Target


# 3Sum (same as Two Sum, use hashmap or sort+pointers)
def three_sum(nums):
    # find element a, b, c that sum to 0
    result = []
    nums.sort()
    for i in range(len(nums) - 2):
        # if there are duplicates, move to the last one
        if i > 0 and nums[i-1] == nums[i]:
            continue
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


# Merge Sorted Array
# assumption: nums1 has extra space to hold all the elements in nums
# m and n are the number of elements in these two static arrays
def merge(nums1, m, nums2, n):
    while m > 0:
        # starting from the right sides
        # index after m+n-1 to be the merged part
        if nums1[m - 1] < nums1[n - 1]:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
        else:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
    # if n == 0 then the pointer has moved n times
    # else nums has n elements smaller than all nums1 elements
    if n > 0:
        for i in range(n):
            nums1[i] = nums2[i]
        

# move zeros to the end of array, do it in-place
def move_zeros(nums):
    if len(nums) <= 1:
        return
    # find the initial index of zero
    p0 = 0
    while p0 < len(nums) and nums[p0] != 0:
        p0 += 1
    # start at the index after zero pointer
    for i in range(p0 + 1, len(nums)):
        if nums[i] != 0:
            nums[i], nums[p0] = nums[p0], nums[i]
            # nums[p0+1] is guaranteed to be 0
            p0 += 1

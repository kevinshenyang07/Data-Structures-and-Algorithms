# Two Sum approach: hashmap or sort + pointers
# Two Sum - Array is Sorted
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


# Merge Sorted Array
# assumption: nums1 has extra space to hold all the elements in nums
# m and n are the number of elements in these two static arrays
def merge(nums1, m, nums2, n):
    # starting from the right sides
    # the index of a certain element can be determined, thus no swap
    while m > 0:
        # index after m-1 to be the merged part
        if nums1[m - 1] < nums1[n - 1]:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
        else:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
    # if n == 0 then the pointer has moved n times
    # else nums has n elements smaller than all nums1 elements
    if n > 0:
        for i in range(n):
            nums1[i] = nums2[i]


# Interleaving Positive and Negative Numbers
# for example, [-1,-2,-3,4,5,6] => [-1,4,-2,5,-3,6]
# do it in place without extra space
def rerange(nums):
    if len(nums) <= 1:
        return
    # count the postive numbers
    num_pos = 0
    for num in nums:
        if num >= 0:
            num_pos += 1
    # determine if the array should start with pos or neg number
    # initialize same-way pointers, if more pos numbers the pointer
    # must start from 0, otherwise will mess up the swapping
    if num_pos * 2 >= len(nums):
        pos, neg = 0, 1
    else:
        neg, pos = 1, 0
    # if either all pos numbers or all neg numbers are in their place,
    # then it's done, the rest are extra neg/pos numbers
    while pos < len(nums) and neg < len(nums):
        if nums[pos] >= 0:  # then the element is in its place
            pos += 2
        elif nums[neg] < 0:
            neg += 2
        else:
            nums[pos], nums[neg] = nums[neg], nums[pos]
# O(n) time, O(1) space


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


# Remove Duplicates from Sorted Array
# returns the length of deduplicated array
def remove_duplicates(nums):
    # have a pointer to the end of deduplicated array
    # 1 2 2 2 3
    # 1 2 3 2 3
    if not nums:
        return 0
    end = 0
    for i in range(len(nums)):
        if nums[i] != nums[end]:
            # add length by one and put the new num at the end
            end += 1
            nums[end] = nums[i]
    return end + 1


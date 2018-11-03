# Kth Largest ELement in an Array
# k to be one-indexed
def find_kth_largest(nums, k):
    if not nums or k < 1 or k > len(nums):
        return 0
    return quick_select(nums, 0, len(nums) - 1, len(nums) - k)
# O(n) time, O(1) space


# Wiggle Sort II
def wiggle_sort(nums):
    n = len(nums)
    k = (n + 1) / 2
    median = quick_select(nums, 0, n - 1, k - 1)

    # three-way partition in particular order
    # weaving them will guarantee correct order (with medians on both side)
    left = []  # use medians first, then numbers < median
    right = []  # use numbers > median first, then medians

    for i, num in enumerate(nums):
        if num < median:
            left.append(num)
        elif num > median:
            right.append(num)

    while len(left) < k:
        left.append(median)

    for i in range(0, n, 2):
        nums[i] = left.pop()

    for i in range(1, n, 2):
        if right:
            nums[i] = right.pop()
        else:
            nums[i] = median  # the rest must be medians
# O(n) time and space


# find kth smallest in range
# k to be zero-indexed
def quick_select(nums, i, j, k):
    while i < j:
        pivot = partition(nums, i, j)
        # narrow the partition range by pivot index
        if pivot < k:
            i = pivot + 1
        elif pivot > k:
            j = pivot - 1
        else:
            break
    return nums[i]

# partition with two pointers, returns a partition index where
# every element on the left is <= nums[i] (pivot value)
# every element on the right is >= nums[i]
def partition(nums, i, j):
    # if using random init pivot, swap to the left anyway
    left = i + 1
    right = j
    # let right cross left to make sure nums[right] < nums[i] in the end
    # left equal to right covers the two elements situation
    while left <= right:
        if nums[left] <= nums[i]:
            left += 1
        elif nums[right] >= nums[i]:
            right -= 1
        # if two pointers haven't crossed yet and ready to swap
        else:
            nums[left], nums[right] = nums[right], nums[left]
    # swap pivot with the rightmost element that is smaller than pivot
    nums[i], nums[right] = nums[right], nums[i]
    return right
# O(n) time, O(n^2) worst case, O(1) space
# the first call of partition takes O(n), the next take an average of O(n/2)...
# worst case happens on selecting maximum on a sorted list, using 0 as pivot index


if __name__ == '__main__':
    print find_kth_largest([1, 2], 1)  # 2
    print find_kth_largest([10, 4, 5, 8, 6, 11, 26], 4)  # 8
    print find_kth_largest([1, 2, 1, 1, 2, 1, 2], 4)  # 1

    nums1 = [1, 1, 2, 1, 2]
    wiggle_sort(nums1)
    print nums1  # [1, 2, 1, 2, 1]

    nums2 = [1, 3, 2, 2, 3, 1]
    wiggle_sort(nums2)
    print nums2 # [2,3,1,3,1,2]

    nums3 = [2, 3,3, 2, 2, 2, 1, 1]
    wiggle_sort(nums3)
    print nums3  # [2,3,2,3,1,2,1,2]
